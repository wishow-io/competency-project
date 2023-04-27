import zipfile
import plotly.express as px
import pandas as pd
from flask import send_file
import json
import os
from constants import *
from server_functions import *


# from a simple dict to a zipfile of radar chart images(mock: user_level): 
def get_dataframe_from_dict(dict):
    # Convert the dictionary to the format expected by px.line_polar
    df = pd.DataFrame({ 
        "values": list(dict.values()), 
        "keys": list(dict.keys())})
    return df

def generate_radar_chart_fig(dataframe,id,family):
    # Convert the dataframe into radar chart figure 
    fig = px.line_polar(dataframe, range_r=[0, 5], r="values", theta="keys", line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'Radar Chart de {id}, famille : {family}')
    return fig

def create_directory_by_id(id):
    if not os.path.exists(f'{dir_images}/{id}/'):
        os.mkdir((f'{dir_images}/{id}/')) 

def convert_fig_to_image(fig,id,family):
    img = fig.write_image(f'{dir_images}/{id}/radar_chart_{id}_{family}_{timestr}.jpeg')
    return img 

def save_img_in_zip_file(id,family):
    # Put image in a zip file
    with zipfile.ZipFile(f'{dir_zip}/zipfile{id}.zip', 'w') as zip_file:
        zip_file.write(f'{dir_images}/{id}/radar_chart_{id}_{family}_{timestr}.jpeg')
        return 


def download_file(id):
    filename = f'{dir_zip}/zipfile{id}.zip'
    path = os.path.join(os.getcwd(), filename)
    return send_file(path,mimetype='application/zip', as_attachment=True, download_name=f'zipfile{id}.zip')


def from_dict_to_zipfile(dict,id,family):
    for family in dict:
        dict_by_family = dict[family] 
        family = family
        dataframe = get_dataframe_from_dict(dict_by_family)
        fig = generate_radar_chart_fig(dataframe,id,family)
        create_directory_by_id(id)
        convert_fig_to_image(fig,id,family)
        save_img_in_zip_file(id,family)
        
        return render_download_button()


def from_dict_to_radar_chart_displayed(dict,id,family):
    dataframe = get_dataframe_from_dict(dict)
    fig = generate_radar_chart_fig(dataframe,id,family)
    create_directory_by_id(id)
    img = convert_fig_to_image(fig,id,family)
    return display_img(img,id,family)



## get the best profile compared with a target profile 
def best_profile(a_dict):

    target_skills = a_dict["target"]
    profiles = a_dict["profiles"]
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


##In progress : divide this function(up)
# def get_score(profile_level, target_level):
#     if profile_level == 0:
#         return - 5
#     bonus_malus = target_level - profile_level
#     return  bonus_malus

# def get_profile_score(profile_skills, target_skills):
#     score = 0 
#     for i in profile_skills : 
#         score += get_profile_score(profile_skills[i], target_skills[i])
#     return score 

# def best_profile(profiles,target_skills):
#     profiles_score = {}
#     for i in profiles:
#         profiles[i["name"]] = get_profile_score(profiles["skills"], target_skills)
#     sorted_dict =dict(sorted(profiles_score.items(), key=lambda x: x[1], reverse=True))
#     sorted_json = json.dumps(sorted_dict)
#     return sorted_json

# def get_best_profile(dict):
#     target_skills = dict["target"]
#     profiles = dict["profiles"]
#     profile_skills = i["skills"]

#     for i in profiles:
#         get_score(profile_skills,)