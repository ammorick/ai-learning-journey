from safe import is_safe
from api1 import call_ai
from concurrent.futures import ThreadPoolExecutor
from memory import load_history,add_message
from safety_logger import  log_violation

def route(question):
    medical_keywords=["感冒","发烧","医学","健康"]
    law_keywords=["法律", "合同", "权益", "官司", "请假", "病假", "拒绝", "公司", "劳动"]
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
    
def get_experts_answers(question,max_rounds=3):
    history=load_history()
    context="\n".join([f"{msg['role']}:{msg['content']}" for msg in history[-10:]])
    enhanced_question=f"历史对话：\n{context}\n\n当前问题{question}"

    if question.strip().startswith("!") or "回顾" in question:
        first_round_question=enhanced_question
    else:
        first_round_question=question

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


    #储存所有轮次的专家问题
    discussion_log=[]  # 每个元素是一个字典 {exp: answer}



    for round_idx in range(max_rounds):
        round_answers={}
        with ThreadPoolExecutor(max_workers=len(expert_list)) as executor:
            future_to_exp={}
            for exp in expert_list:
                prompt=prompts.get(exp,prompts["general"])
                api_name=api_for.get(exp,"zhipu")

                #构造本轮问题
                if round_idx==0:
                    #用上面处理好的 first_round_question做问题
                    round_question=first_round_question

                else:
                    #专家之间的对话，用历史文本框架做对话框
                    history_text=""
                    for i,log in enumerate(discussion_log,1):
                        history_text += f"第{i}轮讨论:\n"
                        for e,ans in log.items():
                            history_text += f"[{e.upper()}专家]:{ans}\n"
                        history_text += "\n"
                    round_question=(
                        f"用户原始问题：{question}\n\n"
                        f"以下是到目前为止的讨论记录:\n{history_text}\n"
                        f"这是第{round_idx+1}轮讨论记录，请参考上述内容，给出你的回答，要求理性，客观，严肃，基于事实或者真实理论，你站在自己的角度，可以认可，不认可，同意、反驳、补充之前的所有观点"

                    )

            
                future=executor.submit(call_ai,prompt,round_question,api_name)
                future_to_exp[future]=exp
            for future in future_to_exp:
                exp=future_to_exp[future]
                try:
                    round_answers[exp]=future.result()
                except Exception as e:
                    round_answers[exp]=f"{exp}专家第{round_idx+1}轮不可用"

        discussion_log.append(round_answers)
        
    return discussion_log[-1]

            




    