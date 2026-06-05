import requests  #导入请求
import os #导入索引

# ---------- 安全检测 ----------
from safe import is_safe
# ---------- 总监----------
from zongjian import summarize
# ---------- 专家映射 ----------
from fenhua import get_experts_answers
#--------------增加并行操作----------
from concurrent.futures import ThreadPoolExecutor
#--------------增加记忆模块------------------
from memory_brain import add_message,load_history
#-------------------拦截日志---------------------
from safety_logger import  log_violation
# ---------- 主程序 ----------

def main():
     print("H E L L O !!!!!")   #打招呼
     print("如果想要退出的话，请输入：exit")
     history=load_history()
     print(f"已加载 {len(history)} 条历史记录")
     while True:
          user_input=input("你的问题：")
          review=["回顾历史","回顾对话","上次对话","之前说了什么"]
          if user_input.lower()=="exit":
               break
          if not user_input.strip():
               continue
          if any(kw in user_input for kw in review):
               answers=get_experts_answers(user_input)
               direct_answer=answers.get("general",list(answers.values())[0] if answers else "无回答")
               print(f"\n{direct_answer}")
               continue
          add_message("user",user_input)
          answers=get_experts_answers(user_input)
          final=summarize(user_input,answers)
          if not is_safe(final):
               log_violation("output", final, "黑名单匹配")
               final = "[安全大脑拦截] 生成的回答包含敏感内容，已自动屏蔽。"
          add_message("assistant",final)
          print(f"\n总监汇总：{final}\n")



if __name__ == "__main__":
    main()