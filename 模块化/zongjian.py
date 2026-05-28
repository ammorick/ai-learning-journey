def director(question):
     medical_director=["感冒","健康","医学"]
     law_director=["法律","合同","权利"]
     experts=[]
     for word in medical_director:
          if word in question:
              experts.append("medical")
              break
     for word in law_director:
          if word in question:
               experts.append("law")
               break
     if not experts:
          return ["general"]
     return experts

          


#目前仅是调动单个大脑，之后会逐步改进成同时调动多个大脑
#比如用生物解释医学问题