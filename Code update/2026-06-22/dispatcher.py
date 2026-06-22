from safe import is_safe
from api1 import call_ai
from concurrent.futures import ThreadPoolExecutor
from memory import load_history,add_message
from safety_logger import  log_violation
import json
import os
from datetime import datetime

expert_config=None
def load_expert_config():
    global expert_config
    config_path=os.path.join(os.path.dirname(__file__),"config","expert_config.json")
    with open(config_path,"r",encoding="utf-8") as f:
        expert_config=json.load(f)


def route(question):
    global expert_config
    matched=[]
    for expert in expert_config["experts"]:
        for keyword in expert["keywords"]:
            if keyword in question:
                matched.append(expert["name"])
                break
    if not matched:
        matched.append("general")

    return matched
        
def get_prompt(expert_name):
    global expert_config
    for expert in expert_config["experts"]:
        if expert["name"]==expert_name:
            return expert["prompt"]
    raise ValueError(f"未找到专家配置:{expert_name}")
    
def get_api(expert_name):
    global expert_config
    for expert in expert_config["experts"]:
        if expert["name"]==expert_name:
            return expert["api"]
    raise ValueError(f"未找到API：{expert_name}")

def save_discussion_log(question,discussion_log):
    try:
        archive_dir="discussion_archive"
        os.makedirs(archive_dir,exist_ok=True)
        timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename=f"discussion_{timestamp}.json"
        filepath=os.path.join(archive_dir,filename)

        data={
            "timestamp":timestamp,
            "question":question,
            "rounds":discussion_log
        }
        with open(filepath,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
    except Exception as e:
        print(f"[警告]讨论记录保存失败:{e}")
        
    
def get_experts_answers(question,max_rounds=3):
    global expert_config
    if expert_config is None:
        load_expert_config()
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

    #储存所有轮次的专家问题
    discussion_log=[]  # 每个元素是一个字典 {exp: answer}



    for round_idx in range(max_rounds):
        round_answers={}
        with ThreadPoolExecutor(max_workers=len(expert_list)) as executor:
            future_to_exp={}
            for exp in expert_list:
                prompt=get_prompt(exp)
                api_name=get_api(exp)

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
        save_discussion_log(question, discussion_log)
        
    return discussion_log[-1]

            




    