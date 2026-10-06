import requests
import os
from dotenv import load_dotenv

load_dotenv()
def call_ai(system_prompt,user_question,api_name,timeout=None):
        default_model={
                "zhipu": "glm-4-flash",
                "siliconflow-deep": "deepseek-ai/DeepSeek-V4-Flash",
                "siliconflow-step": "stepfun-ai/Step-3.5-Flash",        
                "siliconflow-strategy": "Qwen/Qwen3.6-35B-A3B"              
        }
        if api_name.startswith("siliconflow"):
              url = "https://api.siliconflow.cn/v1/chat/completions"
              api_key = os.getenv("SILICONFLOW_API_KEY")

        elif api_name=="zhipu":
              url="https://open.bigmodel.cn/api/paas/v4/chat/completions"
              api_key=os.getenv("ZHIPU_API_KEY")
        else:
              raise ValueError("不支持的API")  
        
        if not api_key:
              raise ValueError(f"环境变量{api_name.upper()}_API_KEY 未设置")
        


        timeout_val=timeout if timeout is not None else 90

              
        headers={
             "Authorization":f"Bearer {api_key}",  #持有Api——Key令牌，获得服务器响应
             "Content-Type":"application/json"   #内容格式是json
          } 

        messages=[
             {"role":"system","content":system_prompt},#系统扮演的角色
             {"role":"user","content":user_question}  #接受用户的问题
             
        ] 
        data={
             "model":default_model[api_name],    #确定模型
             "messages":messages      #确定角色
        }
        try:
             response=requests.post(url,json=data,headers=headers,timeout=timeout_val) #测试响应
             response.raise_for_status()
             result=response.json()
             return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
             raise Exception(f"API调用失败:{api_name}-{str(e)}")
