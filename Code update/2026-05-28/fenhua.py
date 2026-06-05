from anquan import is_safe
from api1 import call_ai
from concurrent.futures import ThreadPoolExecutor

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
    if not is_safe(question):
        return{"safety":"blocked"}
    expert_list=route(question)
    prompts={
        "medical":"你是一位资深医生，请提供专业，可靠的医学建议",
        "law":"你是一位专业的律师，请提供专业，可靠的法律建议",
        "general":"你是一个有用的助手，请友好风趣幽默的回答用户的问题"
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
            future=executor.submit(call_ai,prompt,question,api_name)
            future_to_exp[future]=exp
        for future in future_to_exp:
            exp=future_to_exp[future]
            results[exp]=future.result()
    return results