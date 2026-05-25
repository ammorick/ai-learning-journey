step=0
def aaa(n,A,B,C):
    global step
    if n==1:
        step=step+1
        print(A ,'-->',C)
    else:
        aaa(n-1,A,C,B)
        step=step+1
        print(A ,'-->',C)
        aaa(n-1,B,A,C)
aaa(3,'A','B','C')
print(f"盘子需要移动的次数：{step}")



# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
