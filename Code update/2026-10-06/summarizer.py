from api import call_ai

def summarize(question, answers_dict):
    if "safety" in answers_dict:
        return "抱歉，你的问题涉及敏感词，我无法回答"
    
    parts=[f"用户的问题:{question}"]
    for exp,ans in answers_dict.items():
        parts.append(f"\n [{exp.upper()}专家]\n{ans}")
    system_prompt = "你是一个绝对客观、中立的第三方主持法官。你在这场讨论中没有个人立场，不偏袒任何一方。请严格基于逻辑和证据评估所有专家的发言，哪怕某个观点是你作为专家角色时提出的，也必须一视同仁。"
    summary_prompt="\n".join(parts)+ """

请综合以上各位专家的意见，给出一个全新、清晰、友好的最终回答。如果不同专家观点有差异，请分别说明，帮助用户做出判断"""
    final=call_ai(system_prompt,summary_prompt,"siliconflow-deep")
    return final