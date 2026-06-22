from safe import is_safe
from summarizer import summarize
from dispatcher import get_experts_answers
from memory import add_message, load_history
from safety_logger import log_violation
from random_brain import run_random_dialogue  # 新增导入

def main():
    print("H E L L O !!!!!")
    print("如果想要退出，请输入：exit")
    print("输入 /random 切换至随机大脑对话模式")
    print("输入 /normal 切回普通对话模式")

    history = load_history()
    print(f"已加载 {len(history)} 条历史记录")

    mode = "normal"  # "normal" | "random"
    review_keywords = ["回顾历史", "回顾对话", "上次对话", "之前说了什么"]

    while True:
        user_input = input("\n你的问题：")

        # 模式切换命令
        if user_input == "/random":
            mode = "random"
            print("[系统] 已切换至 随机大脑对话模式")
            continue
        elif user_input == "/normal":
            mode = "normal"
            print("[系统] 已切回 普通对话模式")
            continue
        elif user_input.lower() == "exit":
            break

        if not user_input.strip():
            continue

        # ---------- 随机大脑模式 ----------
        if mode == "random":
            # 解析用户输入是否指定了专家：/random 医学 策略
            parts = user_input.strip().split()
            if parts[0] == "/random" and len(parts) > 1:
                specified = parts[1:]
            else:
                specified = None

            record = run_random_dialogue(specified_experts=specified, max_rounds=3)

            # 由总监大脑汇总最后一轮讨论
            last_round_answers = record["rounds"][-1]
            summary = summarize(record["entry_point"], last_round_answers)

            print(f"\n[总监汇总]\n{summary}")
            print(f"\n[系统] 讨论记录已保存: discussion_archive/random/随机对话_{record['timestamp']}_{'_'.join(record['participants'])}.json")
            continue

        # ---------- 普通对话模式 ----------
        # 回顾历史关键词检测
        if any(kw in user_input for kw in review_keywords):
            answers = get_experts_answers(user_input)
            direct_answer = answers.get("general", list(answers.values())[0] if answers else "无回答")
            print(f"\n{direct_answer}")
            continue

        # 正常对话流程
        add_message("user", user_input)
        answers = get_experts_answers(user_input)
        final = summarize(user_input, answers)

        if not is_safe(final):
            log_violation("output", final, "黑名单匹配")
            final = "[安全大脑拦截] 生成的回答包含敏感内容，已自动屏蔽。"

        add_message("assistant", final)
        print(f"\n总监汇总：{final}\n")

if __name__ == "__main__":
    main()