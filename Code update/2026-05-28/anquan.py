# ---------- 安全检测 ----------
def is_safe(text):
    dangerous=["炸弹", "恐怖", "杀人", "色情", "暴力"]
    for word in dangerous:
        if word in text:
            return False
    return True