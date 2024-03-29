from api.constants import *
from flask import send_file, render_template
import os
from api.utils import *


def display_img(img, id):
    img = f'generated_files/images/{id}/radar_chart_{id}_{timestr}.jpeg'
    return send_file(img, mimetype='image/jpeg')


def download_file(id, filename):
    filename = f'{dir_files_zip}/zipfile{id}.zip'
    path = os.path.join(os.getcwd(), filename)
    return send_file(path, mimetype='application/zip', as_attachment=True, download_name=f'zipfile{id}.zip')
