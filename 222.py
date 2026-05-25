import requests
import os

# ---------- 安全检测（保持原样） ----------
def is_safe(text):
    dangerous = ["炸弹", "恐怖", "杀人", "色情", "暴力"]
    for word in dangerous:
        if word in text:
            return False
    return True

# ---------- 通用AI调用（支持专家角色） ----------
def call_ai(system_prompt, user_question):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, 'key.txt')
    with open(key_path, 'r') as f:
        api_key = f.read().strip()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # 构造消息列表：先系统提示，再用户问题
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]
    data = {
        "model": "glm-4-flash",
        "messages": messages
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"调用AI失败：{e}"

# ---------- 总监路由：根据问题决定调哪一类专家 ----------
def director(question):
    # 你可以填写关键词和对应的专家提示词
    if "医学" in question or "感冒" in question or "健康" in question:
        return "medical"
    elif "法律" in question or "合同" in question or "权利" in question:
        return "law"
    else:
        return "general"

# ---------- 专家映射 ----------
def get_system_prompt(expert_type):
    prompts = {
        "medical": "你是一位资深医生，请提供专业、可靠的医学建议。",
        "law": "你是一位专业律师，请依据法律法规给出建议。",
        "general": "你是一个有用的助手，请友好地回答用户问题。"
    }
    return prompts.get(expert_type, prompts["general"])

# ---------- 主程序 ----------
def main():
    print("=== 安全双专家问答系统 ===")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() == 'quit':
            break
        if not is_safe(user_input):
            print("AI: 抱歉，你的问题包含敏感内容，我无法回答。")
            continue
        expert = director(user_input)
        system_prompt = get_system_prompt(expert)
        answer = call_ai(system_prompt, user_input)
        print(f"AI ({expert}专家): {answer}")

if __name__ == "__main__":
    main()