import requests  #导入请求
import os #导入索引

# ---------- 安全检测 ----------
from anquan import is_safe
# ---------- 通用AI调用（支持专家角色） ----------
from api import call_ai
# ---------- 总监路由：根据问题决定调哪一类专家 ----------
from zongjian import director
# ---------- 专家映射 ----------
from zhuanjia import get_system_prompt
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
          expert_list=director(user_input)  #用用户输入的问题作为材料去寻找答案
          answers=[]
          for expert in expert_list:
               system_prompt=get_system_prompt(expert)   #系统类型，引擎，形象
               answer=call_ai(system_prompt,user_input)   #索引来的答案
               answers.append(f"[{expert}专家]{answer}")
          final_answer="\n".join(answers)
          print(f"AI 综合回答：\n{final_answer}")   #打印出来

if __name__=="__main__":
     main()
