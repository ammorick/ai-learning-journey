def get_system_prompt(expert_type):
     prompts = {
        "medical": "你是一位资深医生，请提供专业、可靠的医学建议。",
        "law": "你是一位专业律师，请依据法律法规给出建议。",
        "general": "你是一个有用的助手，请友好风趣幽默的回答用户的问题。"
    }
     return prompts.get(expert_type,prompts["general"])