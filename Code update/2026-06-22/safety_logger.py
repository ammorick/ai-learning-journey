import os
from datetime import datetime

# 日志目录和文件路径（相对于本文件所在目录）
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "safety.log")

def log_violation(violation_type, content, reason):
    """
    记录安全拦截事件。

    参数:
        violation_type (str): 拦截类型，例如 "input"（用户输入）或 "output"（AI回答）
        content (str): 被拦截的具体内容
        reason (str): 拦截原因，例如 "黑名单匹配：炸弹"
    """
    # 确保日志目录存在（如果不存在则创建）
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # 生成时间戳
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 以追加模式打开日志文件，写入记录
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{violation_type}] {reason}\n")
        f.write(f"  Content: {content}\n")
        f.write("-" * 60 + "\n")