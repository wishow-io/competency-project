import zipfile
import plotly.express as px
import pandas as pd
from flask import send_file
import json


#save jpeg of the radar chart in zipfile
def generate_zipfile_by_family():
#mock
    dict = {
    "1": {
    
        "Debugging & Observability": {
            "Debugging":"1",
            "Observability":"4"
        },

        "Quality & testing": {
            "écriture de code":"4",
            "testing":"3"
        },

        "Software design & architecure ": {
            "understanding code":"2"
        },
    },

    "2": {

        "Debugging & Observability": {
            "Debugging":"3",
            "Observability":"5"
        },

        "Quality & testing":{
            "écriture de code":"3",
            "testing":"2"
        },

        "Software design & architecure ": {
        "understanding code":"2"
        },
    }
}
    for i in dict:
        with zipfile.ZipFile(f'myzipfile{i}.zip', 'w') as zip_file:
            for j in dict[i]:
                dict[i][j] = {
                    "values": list(dict[i][j].values()),
                    "keys":list(dict[i][j].keys())
                    }  
                print(dict[i][j]) 
                df = pd.DataFrame(dict[i][j])
                fig = px.line_polar(df,r="values",theta="keys",line_close=True)
                fig.update_layout(title=f'Radar de {i} pour {j}')
                fig.write_image(f'images/radar_{i} {j}.jpeg')
                if not os.path.exists(f'myzipfile{i}'):
                    zip_file.write(f'images/radar_{i} {j}.jpeg')
                    os.remove(f'images/radar_{i} {j}.jpeg')
    return "Zip file created"



def generate_radar_chart_image():
    input_dict = {
        "Debugging": 1,
        "Observability": 4,
        "écriture de code": 3,
        "testing": 2,
        "understanding code": 2
    }

    # Normalize input_dict values to range 0-5
    max_val = max(input_dict.values())
    normalized_dict = {k: v / max_val * 5 for k, v in input_dict.items()}

    # Convert the dictionary to the format expected by px.line_polar
    data = {
        "values": list(normalized_dict.values()),
        "keys": list(normalized_dict.keys())
    }
    df = pd.DataFrame(data)

    # Generate the radar chart
    fig = px.line_polar(df, range_r=[0, 5], r="values", theta="keys", line_close=True)
    fig.update_traces(fill='toself')
    fig.write_image('images/radar_chart.jpeg')
    filename = 'images/radar_chart.jpeg'
    return send_file(filename, mimetype='image/jpeg')


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
    sorted_json = json.dumps(sorted_dict)
    return sorted_json


