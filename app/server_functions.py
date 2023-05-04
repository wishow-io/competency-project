from constants import *
from flask import send_file, render_template
import os
from utils import *


def display_img(img, id, family):
    # display image on html
    img = f'generated_files/images/{id}/radar_chart_{id}_{family}_{timestr}.jpeg'
    return send_file(img, mimetype='image/jpeg')


def render_download_button():
    return render_template('download.html')


def download_file(id):
    filename = f'{dir_files_zip}/zipfile{id}.zip'
    path = os.path.join(os.getcwd(), filename)
    return send_file(path,mimetype='application/zip', as_attachment=True, download_name=f'zipfile{id}.zip')

