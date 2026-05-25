import requests  #导入请求
import os #导入索引

# ---------- 安全检测 ----------
def is_safe(text):
    dangerous=["炸弹", "恐怖", "杀人", "色情", "暴力"]
    for word in dangerous:
        if word in text:
            return False
    return True

# ---------- 通用AI调用（支持专家角色） ----------
def call_ai(system_prompt,user_question):
        url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"#需要访问的网址
        script_dir=os.path.dirname(os.path.abspath(__file__))
        key_path=os.path.join(script_dir,'key.txt')#自动索取key文件
        with open(key_path,'r') as f:#以只读形式打开文件，并且变成‘f’
             api_key=f.read().strip()#读取f里的字符串
#拿到api key
        headers={
             "Authorization":f"Bearer {api_key}",  #持有Api——Key令牌，获得服务器响应
             "Content-Type":"application/json"   #内容格式是json
          } 

        messages=[
             {"role":"system","content":system_prompt},#系统扮演的角色
             {"role":"user","content":user_question}  #接受用户的问题
             
        ] 
        data={
             "model":"glm-4-flash",    #确定模型
             "messages":messages      #确定角色
        }
        try:
             response=requests.post(url,json=data,headers=headers,timeout=15) #测试响应
             result=response.json()
             return result['choices'][0]['message']['content']
        except Exception as e:
             return f"调用AI失败:{e}"

# ---------- 总监路由：根据问题决定调哪一类专家 ----------
def director(question):
     if "医学" in question or "感冒" in question or "健康" in question:
          return "medical"      #有以上词汇，调动医学大脑
     elif "法律" in question or "合同" in question or "权利" in question:
        return "law"            #有以上词汇，调动法律大脑
     else:
          return "general"       #都没有，调动通用大脑
#目前仅是调动单个大脑，之后会逐步改进成同时调动多个大脑
#比如用生物解释医学问题

# ---------- 专家映射 ----------
def get_system_prompt(expert_type):
     prompts = {
        "medical": "你是一位资深医生，请提供专业、可靠的医学建议。",
        "law": "你是一位专业律师，请依据法律法规给出建议。",
        "general": "你是一个有用的助手，请友好地回答用户问题。"
    }
     return prompts.get(expert_type,prompts["general"])


# ---------- 主程序 ----------
def main():
     print("H E L L O !!!!!")   #打招呼
     print("如果想要退出的话，请输入：exit")
     while True:
          user_input=input("\n 你的问题：")    #用户输入问题
          if user_input.lower()=='exit':    #用户结束
               break
          if not is_safe(user_input):     #违反安全大脑
               print("AI:抱歉，你输入的内容涉及敏感问题，我无法回答。请换个问题提问吧")
               continue
          expert=director(user_input)   #用用户输入的问题作为材料去寻找答案
          system_prompt=get_system_prompt(expert)   #系统类型，引擎，形象
          answer=call_ai(system_prompt,user_input)   #索引来的答案
          print(f"AI({expert}专家)的回答：{answer}")   #打印出来

if __name__=="__main__":
     main()
