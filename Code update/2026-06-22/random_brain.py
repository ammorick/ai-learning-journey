import random
import json
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from api1 import call_ai
from safe import is_safe

# ---------- 常量 ----------
# 第一轮提示词（保持不变）
RANDOM_ARCHIVE_DIR = "discussion_archive/random"
RANDOM_PROMPT_ROUND1_TEMPLATE = """
你是一位富有探索欲的{expert_title}，专注于研究本行业与其他行业之间存在的未知可能性。
请基于你的行业知识，提出几个你认为最有潜力的跨行业交叉方向。
不需要深入展开，只需要提出方向并简要说明为什么值得探索。
"""

RANDOM_PROMPT_ROUND2_TEMPLATE = """
你是一位富有探索欲的{expert_title}，专注于研究本行业与其他行业之间存在的未知可能性。

上一轮讨论中，其他专家提出了以下方向：
{other_experts_summary}

请基于你的行业知识，结合以上观点，提出你的见解。
你可以引用或延续这些方向，也可以提出新的方向——请保持独立判断。
"""
# ---------- 全局配置 ----------
_random_config = None

def load_random_config():
    """加载随机大脑花名册"""
    global _random_config
    config_path = os.path.join(os.path.dirname(__file__), "config", "random_config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        _random_config = json.load(f)
    return _random_config

def get_expert_by_name(expert_name):
    """根据专家名称获取专家配置"""
    global _random_config
    if _random_config is None:
        load_random_config()
    for expert in _random_config.get("experts", []):
        if expert["name"] == expert_name:
            return expert
    return None

def get_api_for_expert(expert_name):
    """根据专家名称获取对应的 API 名称"""
    global _random_config
    if _random_config is None:
        load_random_config()
    for expert in _random_config.get("experts", []):
        if expert["name"] == expert_name:
            return expert.get("api", "zhipu")
    return "zhipu"

def get_expert_title(expert_name):
    """根据专家名称获取标题（用于提示词）"""
    global _random_config
    if _random_config is None:
        load_random_config()
    for expert in _random_config.get("experts", []):
        if expert["name"] == expert_name:
            return expert.get("title", expert_name)
    return expert_name

def list_all_expert_names():
    """获取所有专家名称列表"""
    global _random_config
    if _random_config is None:
        load_random_config()
    return [e["name"] for e in _random_config.get("experts", [])]

def select_participants(specified=None, count=None):
    """选择参与随机对话的专家"""
    all_names = list_all_expert_names()
    if not all_names:
        raise ValueError("花名册为空，无法选择参与者")
    if specified:
        valid = [name for name in specified if name in all_names]
        if not valid:
            raise ValueError(f"指定的专家均不在花名册中: {specified}")
        return valid
    if count is None:
        count = random.randint(2, 3)
    if count > len(all_names):
        count = len(all_names)
    return random.sample(all_names, count)

def generate_entry_point():
    """生成随机对话的切入点主题"""
    return "跨行业新可能性探索"

def run_random_dialogue(specified_experts=None, max_rounds=3):
    """
    执行一次完整的随机大脑对话
    - specified_experts: 指定专家名称列表，若不传则随机选择
    - max_rounds: 最多讨论轮数
    返回：讨论记录字典
    """
    participants = select_participants(specified_experts)
    print(f"[随机大脑] 参与专家: {participants}")

    discussion_log = []
    full_history_text = f"讨论主题：{generate_entry_point()}\n\n"
    entry_point = generate_entry_point()

    for round_idx in range(max_rounds):
        round_answers = {}
        with ThreadPoolExecutor(max_workers=len(participants)) as executor:
            future_to_exp = {}
            for exp_name in participants:
                title = get_expert_title(exp_name)
                api_name = get_api_for_expert(exp_name)

                # ---------- 根据轮次选择不同的提示词模板 ----------
                if round_idx == 0:
                    # 第一轮：保留你加了“之间”的版本
                    prompt = RANDOM_PROMPT_ROUND1_TEMPLATE.format(expert_title=title)
                    question = f"讨论主题：{entry_point}\n\n请基于你的行业知识，提出几个你认为最有潜力的跨行业交叉方向。不需要深入展开，只需要提出方向并简要说明为什么值得探索。"

                else:
                    # 第二轮及以后：提取上一轮其他专家的发言摘要
                    prev_round = discussion_log[-1] if discussion_log else {}
                    other_summary = ""
                    for exp, ans in prev_round.items():
                        if exp != exp_name:
                            # 取前200字符作为摘要，避免token过多
                            summary = ans[:200] + "..." if len(ans) > 200 else ans
                            other_summary += f"[{exp}]: {summary}\n"
                    if not other_summary:
                        other_summary = "（上一轮暂无其他专家发言）"

                    prompt = RANDOM_PROMPT_ROUND2_TEMPLATE.format(
                        expert_title=title,
                        other_experts_summary=other_summary
                    )
                    question = f"讨论主题：{entry_point}\n\n这是第{round_idx+1}轮讨论，请参考上一轮其他专家的观点，结合你的行业知识，提出你的见解。"

                future = executor.submit(call_ai, prompt, question, api_name)
                future_to_exp[future] = exp_name

            for future in future_to_exp:
                exp_name = future_to_exp[future]
                try:
                    round_answers[exp_name] = future.result()
                except Exception as e:
                    round_answers[exp_name] = f"[{exp_name}本轮发言失败: {e}]"

        discussion_log.append(round_answers)

        # 更新历史文本
        round_text = f"第{round_idx+1}轮讨论：\n"
        for exp, ans in round_answers.items():
            round_text += f"[{exp}]: {ans}\n"
        round_text += "\n"
        full_history_text += round_text

    # 构建并保存记录
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    participants_str = "_".join(participants)
    record = {
        "timestamp": timestamp,
        "participants": participants,
        "entry_point": entry_point,
        "rounds": discussion_log,
        "full_history": full_history_text
    }

    os.makedirs(RANDOM_ARCHIVE_DIR, exist_ok=True)
    filename = f"随机对话_{timestamp}_{participants_str}.json"
    filepath = os.path.join(RANDOM_ARCHIVE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    return record