import zipfile
import json
import os
from constants import *
from utils import *
from server_functions import *
from json2html import *
import plotly.graph_objects as go


def generate_radar_chart_fig(data_dict,id):
    score = list(data_dict.values())
    skills = list(data_dict.keys())
    fig = go.Figure(data=go.Scatterpolar(
    r=score,
    theta=skills,
    fill='toself'
    ))
    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True, range=[0, 5]
        )),
    title=f'Radar Chart de {id}',
    showlegend=False
    )
    return fig

#alternative to radar chart when only two values to show
def generate_polar_bar_chart_fig(data_dict,id,family):
    score = list(data_dict.values())
    int_score = [int(x) for x in score]
    skills = list(data_dict.keys())
    fig = go.Figure()
    fig.add_trace(go.Barpolar(
        r=int_score,
        theta=skills,
        width=[0.4, 0.4],
        marker=dict(
            line=dict(
                width=1)
        ),
        name='Skills'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),title=f'Polar bar chart de {id}, famille : {family}',
        showlegend=False
    )
    return fig


def save_img_in_file(fig,id):
    dir_id = f'{id}'
    if not os.path.exists(dir_files):
        os.mkdir(dir_files)
    if not os.path.exists(dir_files_images):
        os.mkdir(dir_files_images)
    dir_files_images_id = os.path.join(dir_files_images,dir_id)
    if not os.path.exists(dir_files_images_id):
        os.mkdir(dir_files_images_id)    
    path = f'radar_chart_{id}_{timestr}.jpeg'
    os.path.join(dir_files_images_id,path)
    img = fig.write_image(f'{dir_files_images_id}/radar_chart_{id}_{timestr}.jpeg')
    return img

    

def from_dict_to_zipfile(data_dict, id,family):
    if not os.path.exists(dir_files_zip):
        os.mkdir(dir_files_zip)
    with zipfile.ZipFile(f'{dir_files_zip}/zipfile{id}.zip', 'w') as zip_file:
        for family, dict_by_family in data_dict.items():
            fig = generate_polar_bar_chart_fig(dict_by_family, id, family)
            create_files_zip_dir()
            fig.write_image(f'polar_bar_chart_{id}_{family}_{timestr}.jpeg')
            zip_file.write(f'polar_bar_chart_{id}_{family}_{timestr}.jpeg')
            os.remove(f'polar_bar_chart_{id}_{family}_{timestr}.jpeg')
    return render_download_button() 

def from_dict_to_radar_chart_displayed(data_dict,id):
    fig = generate_radar_chart_fig(data_dict,id)
    img = save_img_in_file(fig,id)
    return display_img(img,id)



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
    response = json2html.convert(json = sorted_json)
    return response

