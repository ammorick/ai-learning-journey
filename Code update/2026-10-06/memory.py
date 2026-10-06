import json
import os

DEFAULT_USER = "default"
DEFAULT_SESSION = "default"
DEFAULT_DIALOGUE="default"
def _get_file_path(dialogue_type=None,user_id=None,session_id=None):
# """根据多大脑对话问题，用户ID和会话ID生成文件路径，如果未提供则使用默认值"""
    if dialogue_type is None:
        dialogue_type=DEFAULT_DIALOGUE
    if user_id is None:
        user_id=DEFAULT_USER
    if session_id is None:
        session_id = DEFAULT_SESSION
    return f"memory_{dialogue_type}_{user_id}_{session_id}.json"

def load_history(dialogue_type=None,user_id=None,session_id=None):
    file_path=_get_file_path(dialogue_type,user_id,session_id)
    if not os.path.exists(file_path):
        return []
    with open(file_path,"r",encoding="utf-8") as f:
        return json.load(f)
    
def save_history(history,dialogue_type=None,user_id=None,session_id=None):
    file_path=_get_file_path(dialogue_type,user_id,session_id)
    with open (file_path,"w",encoding="utf-8") as f:
        json.dump(history,f,ensure_ascii=False,indent=2)

def add_message(role,content,max_history=20,dialogue_type=None,user_id=None,session_id=None):
    history=load_history(dialogue_type,user_id,session_id)
    history.append({"role":role,"content":content})
    if len(history)>max_history:
        history=history[-max_history:]
    save_history(history,dialogue_type,user_id,session_id)

