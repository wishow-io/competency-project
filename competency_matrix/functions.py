import zipfile
import plotly.express as px
import pandas as pd
from flask import send_file, render_template
import json
import os
from utils import *
import time

#variable to have date in file name
timestr = time.strftime("%Y%m%d-%H%M%S")


## from a simple dict to a zipfile of radar chart images (mock data : user_level): 

def get_dataframe_from_dict(dict):
    # Convert the dictionary to the format expected by px.line_polar
    data = {
        "values": list(dict.values()),
        "keys": list(dict.keys())
    }
    dataframe = pd.DataFrame(data)
    return dataframe

def generate_radar_chart_fig(dataframe,id,family):
    #convert the dataframe into radar chart figure 
    fig = px.line_polar(dataframe, range_r=[0, 5], r="values", theta="keys", line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(title=f'Radar Chart de {id}, famille : {family}')
    return fig

def convert_fig_to_img_saved(fig,id,family):
    #convert the figure of radar chart into a jpeg image
    if not os.path.exists(f'images/{id}/'):
        os.mkdir(f'images/{id}/')  
    img = fig.write_image(f'images/{id}/radar_chart_{id}_{family}_{timestr}.jpeg')
    return img 


def display_img(img,id,family):
    #display image on html 
    img = f'images/{id}/radar_chart_{id}_{family}_{timestr}.jpeg'
    return send_file(img, mimetype='image/jpeg')

def save_img_in_zip_file(id,family):
    #put my image in a zip file
    with zipfile.ZipFile(f'zip/zipfile{id}.zip', 'w') as zip_file:
        zip_file.write(f'images/{id}/radar_chart_{id}_{family}_{timestr}.jpeg')
        return 

def render_download_button():
    return render_template('download.html')
    

def download_file(id):
    filename = f'zip/zipfile{id}.zip'
    path = os.path.join(os.getcwd(), filename)
    return send_file(path,mimetype='application/zip', as_attachment=True, download_name=f'zipfile{id}.zip')

def from_dict_to_zipfile(dict,id,family):
  
    for family in dict:
        dict_by_family = dict[family] 
        family = family
        dataframe = get_dataframe_from_dict(dict_by_family)
        fig = generate_radar_chart_fig(dataframe,id,family)
        convert_fig_to_img_saved(fig,id,family)
        save_img_in_zip_file(id,family)
        
        return render_download_button()


def from_dict_to_radar_chart_displayed(dict,id,family):
    dataframe = get_dataframe_from_dict(dict)
    fig = generate_radar_chart_fig(dataframe,id,family)
    img = convert_fig_to_img_saved(fig,id,family)
    return display_img(img,id,family)


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


