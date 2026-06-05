import json
import os

default_file="memory.json"
def load_history(file_path=None):
    if file_path is None:
        file_path=default_file
    if not os.path.exists(file_path):
        return []
    with open(file_path,"r",encoding="utf-8") as f:
        return json.load(f)
    
def save_history(history,file_path=None):
    if file_path is None:
        file_path=default_file
    with open (file_path,"w",encoding="utf-8") as f:
        json.dump(history,f,ensure_ascii=False,indent=2)

def add_message(role,content,max_history=20,file_path=None):
    history=load_history(file_path)
    history.append({"role":role,"content":content})
    if len(history)>max_history:
        history=history[-max_history:]
    save_history(history,file_path)

