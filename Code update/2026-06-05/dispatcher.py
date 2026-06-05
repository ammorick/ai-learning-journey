from safe import is_safe
from api1 import call_ai
from concurrent.futures import ThreadPoolExecutor
from memory import load_history,add_message
from safety_logger import  log_violation

def route(question):
    medical_keywords=["感冒","发烧","医学","健康"]
    law_keywords=["法律","合同","权益","官司"]
    experts=[]
    for word in medical_keywords:
        if word in question:
            experts.append("medical")
            break
    for word in law_keywords:
        if word in question:
            experts.append("law")
            break
    if not experts:
        experts.append("general")
    return experts
    
def get_experts_answers(question):
    history=load_history()
    context="\n".join([f"{msg['role']}:{msg['content']}" for msg in history[-10:]])
    enhanced_question=f"历史对话：\n{context}\n\n当前问题{question}"
    if not is_safe(question):
        log_violation("input", question, "黑名单匹配")
        return{"safety":"blocked"}
    expert_list=route(question)
    prompts={
        "medical":"你是一位资深医生，请提供专业，可靠的医学建议",
        "law":"你是一位专业的律师，请提供专业，可靠的法律建议",
        "general":"你是一个有用的，幽默风趣的助手。如果需要你根据【历史对话】来回答问题，请严格基于以下提供的【历史对话】来回答用户的问题。如果历史对话中没有相关信息，请直接说'没有找到相关历史记录'，绝对不要编造"
    }

    api_for={
        "medical":"zhipu",
        "law":"aliyun",
        "general":"zhipu"
    }

    results={}

    
    with ThreadPoolExecutor(max_workers=len(expert_list)) as executor:
        future_to_exp={}
        for exp in expert_list:
            prompt=prompts.get(exp,prompts["general"])
            api_name=api_for.get(exp,"zhipu")
            future=executor.submit(call_ai,prompt,enhanced_question,api_name)
            future_to_exp[future]=exp
        for future in future_to_exp:
            exp=future_to_exp[future]
            try:
                results[exp]=future.result()
            except Exception as e:
                results[exp]=f"[{exp}专家暂时不可用，原因:{str(e)}]"
    return results