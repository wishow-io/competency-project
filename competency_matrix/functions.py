import zipfile
import plotly.express as px
import pandas as pd
from flask import send_file
import json
import os


## from a simple dict to a zipfile of radar chart images (mock data : user_level): 

def get_dataframe_from_dict(dict):
    # Convert the dictionary to the format expected by px.line_polar
    data = {
        "values": list(dict.values()),
        "keys": list(dict.keys())
    }
    dataframe = pd.DataFrame(data)
    print(dataframe)
    return dataframe

def generate_radar_chart_fig(dataframe,id):
    #convert the dataframe into radar chart figure 
    fig = px.line_polar(dataframe, range_r=[0, 5], r="values", theta="keys", line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'Radar de {id}')
    return fig

def convert_fig_to_img_saved(fig,id):
    #convert the figure of radar chart into a jpeg image
    img = fig.write_image(f'images/radar_chart_{id}.jpeg')
    return img 

def display_img(img,id):
    #display image on html 
    img = f'images/radar_chart_{id}.jpeg'
    return send_file(img, mimetype='image/jpeg')

def save_img_in_zip_file(id):
     #put my image in a zip file 
     with zipfile.ZipFile(f'myzipfile{id}.zip', 'w') as zip_file:
        if not os.path.exists(f'myzipfile{id}'):
            zip_file.write(f'images/radar_chart_{id}.jpeg')
            os.remove(f'images/radar_{id}.jpeg')


def from_dict_to_zipfile(dict,id):
    dataframe = get_dataframe_from_dict(dict)
    fig = generate_radar_chart_fig(dataframe,id)
    img = convert_fig_to_img_saved(fig,id)
    display_img(img,id)
    save_img_in_zip_file(id)

def from_dict_to_radar_chart_displayed(dict,id):
    dataframe = get_dataframe_from_dict(dict)
    fig = generate_radar_chart_fig(dataframe,id)
    img = convert_fig_to_img_saved(fig,id)
    display_img(img,id)


## get the best profile compared with a target profile 

def best_profile(dict):

    target_skills = dict["target"]
    profiles = dict["profiles"]
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


