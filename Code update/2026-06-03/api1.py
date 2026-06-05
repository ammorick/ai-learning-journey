import requests
import os

def call_ai(system_prompt,user_question,api_name):
        default_model={
                "zhipu":"glm-4.5-air",
                "aliyun":"qwen-turbo"
        }
        script_dir=os.path.dirname(os.path.abspath(__file__))
        if api_name=="zhipu":
              url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"#需要访问的网址
              key_path=os.path.join(script_dir,'key.txt')#自动索取key文件

        elif api_name=="aliyun":
              url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
              key_path=os.path.join(script_dir,'key1.txt')#自动索取key文件

        else:
              raise ValueError("不支持的API")  
        
        with open(key_path,'r') as f:
             api_key=f.read().strip()

              
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
             response=requests.post(url,json=data,headers=headers,timeout=90) #测试响应
             result=response.json()
             return result['choices'][0]['message']['content']
        except Exception as e:
             return f"调用AI失败:{e}"
