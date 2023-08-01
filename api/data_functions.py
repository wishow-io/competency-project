import zipfile
import json
import os
from api.constants import *
from api.utils import *
from api.server_functions import *
from json2html import *
import plotly.graph_objects as go


def generate_radar_chart_fig(data_dict):
    score = list(data_dict.get('data').values())
    skills = list(data_dict.get('data').keys())
    fig = go.Figure(data=go.Scatterpolar(
        r=score,
        theta=skills,
        fill='toself'
    ))
    name = data_dict.get('name')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, range=[0, 5]
            )),
        title=f'Radar Chart de {name}',
        showlegend=False
    )
    return fig

# alternative to radar chart when only two values to show


def generate_polar_bar_chart_fig(data_dict, name, family):
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
            )), title=f'Polar bar chart de {name}, famille : {family}',
        showlegend=False
    )
    return fig


def save_img_in_file(fig, id):
    dir_id = f'{id}'
    if not os.path.exists(dir_files):
        os.mkdir(dir_files)
    if not os.path.exists(dir_files_images):
        os.mkdir(dir_files_images)
    dir_files_images_id = os.path.join(dir_files_images, dir_id)
    if not os.path.exists(dir_files_images_id):
        os.mkdir(dir_files_images_id)
    path = f'radar_chart_{id}_{timestr}.jpeg'
    os.path.join(dir_files_images_id, path)
    img = fig.write_image(
        f'{dir_files_images_id}/radar_chart_{id}_{timestr}.jpeg')
    return img


def from_dict_to_zipfile(data_dict, id):
    if not os.path.exists(dir_files_zip):
        os.mkdir(dir_files_zip)
    name = data_dict.get("name")
    with zipfile.ZipFile(f'{dir_files_zip}/zipfile{id}.zip', 'w') as zip_file:
        for family, dict_by_family in data_dict.get("data").items():
            fig = generate_polar_bar_chart_fig(dict_by_family, name, family)
            create_files_zip_dir()
            filename = f'polar_bar_chart_{id}_{family}_{timestr}.jpeg'
            fig.write_image(filename)
            with open(filename, 'rb') as file:
                jpeg_data = file.read()
            zip_file.writestr(filename, jpeg_data)
            os.remove(filename)

    return download_file(id, filename)


def from_dict_to_radar_chart_displayed(data_dict, id):
    fig = generate_radar_chart_fig(data_dict)
    img = save_img_in_file(fig, id)
    return display_img(img, id)


# get the best profile compared with a target profile
def calculate_bonus_score(profile_skills, target_skills):
    bonus_score = []
    for skill, value in profile_skills.items():
        if skill in target_skills:
            if value >= target_skills[skill]:
                bonus_result = value - target_skills[skill]
                bonus_score.append(bonus_result)
    return sum(bonus_score)


def calculate_malus_score(profile_skills, target_skills):
    malus_score = []
    for skill, value in profile_skills.items():
        if skill in target_skills:
            if value == 0:
                malus_score.append(5)
            elif value < target_skills[skill]:
                malus_result = target_skills[skill] - value
                malus_score.append(malus_result)
    return sum(malus_score)


def calculate_final_score(profile, target_skills):
    profile_skills = profile["skills"]
    bonus_sum = calculate_bonus_score(profile_skills, target_skills)
    malus_sum = calculate_malus_score(profile_skills, target_skills)
    final_score = bonus_sum - malus_sum
    return final_score


def best_profile(a_dict):
    target_skills = a_dict["target"]
    profiles = a_dict["profiles"]
    all_final_scores = []
    names = []

    for profile in profiles:
        name = profile["name"]
        names.append(name)
        final_score = calculate_final_score(profile, target_skills)
        all_final_scores.append(final_score)

    final_scores_dict = dict(zip(names, all_final_scores))
    sorted_dict = dict(sorted(final_scores_dict.items(),
                       key=lambda x: x[1], reverse=True))
    top_three = list(sorted_dict.items())[:3]
    result = {
        "target": {
            "score": target_skills
        },
        "ranking": {
            "first": {
                "name": top_three[0][0],
                "score": top_three[0][1]
            },
            "second": {
                "name": top_three[1][0],
                "score": top_three[1][1]
            },
            "third": {
                "name": top_three[2][0],
                "score": top_three[2][1]
            }
        }
    }

    sorted_json = json.dumps(result)
    return sorted_json
