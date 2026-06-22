from api1 import call_ai

def summarize(question, answers_dict):
    if "safety" in answers_dict:
        return "抱歉，你的问题涉及敏感词，我无法回答"
    
    parts=[f"用户的问题:{question}"]
    for exp,ans in answers_dict.items():
        parts.append(f"\n [{exp.upper()}专家]\n{ans}")
    summary_prompt="\n".join(parts)+ """

请综合以上各位专家的意见，给出一个全新，清晰，友好的最终回答。如果不同专家观点有差异，请分别说明，帮助用户做出判断。"""
    final=call_ai("你是一个客观、中立的总结助手。",summary_prompt,"zhipu")
    return final