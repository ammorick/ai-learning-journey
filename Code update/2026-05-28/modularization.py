import requests  #导入请求
import os #导入索引

# ---------- 安全检测 ----------
from anquan import is_safe
# ---------- 通用AI调用（支持专家角色） ----------
from api1 import call_ai

# ---------- 总监----------
from zongjian import summarize
# ---------- 专家映射 ----------
from fenhua import get_experts_answers
#--------------增加并行操作----------
from concurrent.futures import ThreadPoolExecutor

# ---------- 主程序 ----------

def main():
     print("H E L L O !!!!!")   #打招呼
     print("如果想要退出的话，请输入：exit")
     while True:
          user_input=input("你的问题：")
          if user_input.lower()=="exit":
               break
          if not user_input.strip():
               continue
          answers=get_experts_answers(user_input)
          final=summarize(user_input,answers)
          print(f"\n总监汇总：{final}\n")



if __name__ == "__main__":
    main()