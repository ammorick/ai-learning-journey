# ---------- 安全检测 ----------
import json
import os

_config=None
def load_config():
    global _config
    config_path=os.path.join(os.path.dirname(__file__),"config","safety_rules.json")
    with open(config_path,"r",encoding="utf-8") as f:
        _config=json.load(f)
    return _config


def is_safe(text):
    global _config
    if _config is None:
        load_config()

    for word in _config.get("whitelist",[]):
        if word in text:
            return True
    for word in _config.get("blacklist",[]):
        if word in text:
            return False
    return True


