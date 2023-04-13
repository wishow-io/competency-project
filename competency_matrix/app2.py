# Profile type avec score 

mydict = {
    "target": {
        "skill1": 4,
        "skill2": 3,
        "skill3": 3,
        "skill4": 5,
        "skill5": 4
    },
    "profiles": [
        {
            "name": "sdfsf sdfsfsdf",
            "skills": {
                "skill1": 4,
                "skill2": 2,
                "skill3": 2,
                "skill4": 5,
                "skill5": 5
            }
        },
        {
            "name": "ythfgh cccccc",
            "skills": {
                "skill1": 5,
                "skill2": 5,
                "skill3": 5,
                "skill4": 0,
                "skill5": 4
            }
        },
        {
            "name": "fdsfsfd fsfsf",
            "skills": {
                "skill1": 4,
                "skill2": 3,
                "skill3": 4,
                "skill4": 4,
                "skill5": 4
            }
        }
    ]
}
def best_profile():
    mydict = {
    "target": {
        "skill1": 4,
        "skill2": 3,
        "skill3": 3,
        "skill4": 5,
        "skill5": 4
    },
    "profiles": [
        {
            "name": "sdfsf sdfsfsdf",
            "skills": {
                "skill1": 4,
                "skill2": 2,
                "skill3": 2,
                "skill4": 5,
                "skill5": 5
            }
        },
        {
            "name": "ythfgh cccccc",
            "skills": {
                "skill1": 5,
                "skill2": 5,
                "skill3": 5,
                "skill4": 0,
                "skill5": 4
            }
        },
        {
            "name": "fdsfsfd fsfsf",
            "skills": {
                "skill1": 4,
                "skill2": 3,
                "skill3": 4,
                "skill4": 4,
                "skill5": 4
            }
        }
    ]
}
    target_skills = mydict["target"]
    profiles = mydict["profiles"]
    all_final_scores = []
    names = []
    
    for i in profiles:
        name = i["name"]
        names.append(name)
        profile_skills = i["skills"]
        bonus_score = []
        malus_score = []
        for j in profile_skills:
            if j in target_skills:
                print('p',profile_skills[j],'t', target_skills[j])
                if profile_skills[j] == 0 :
                    malus_score.append(5)   
                elif profile_skills[j] >= target_skills[j]:
                    bonus_result = profile_skills[j] - target_skills[j]
                    bonus_score.append(bonus_result)     
                else:
                    malus_result = target_skills[j] - profile_skills[j]
                    malus_score.append(malus_result)
        bonus_sum = sum(bonus_score)
        malus_sum = sum(malus_score)
        final_score = bonus_sum - malus_sum
        all_final_scores.append(final_score)
    final_scores_dict = dict(zip(names,all_final_scores))
    sorted_dict = dict(sorted(final_scores_dict.items(),key=lambda x: x[1],reverse=True))
    print(sorted_dict)
    return sorted_dict

best_profile()
##concat nom + final score in a dict ? 
      

