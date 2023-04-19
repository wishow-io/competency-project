
from flask import Flask
import os
from functions import *
from mock_data.user_score import *

#creating folder images
if not os.path.exists("images"):
    os.mkdir("images")


app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return 'hello from server'

@app.route('/get_zip_by_user/')
def get_zip_by_user():
    id = id
    family= family
    dict =  user_level_by_family
    return from_dict_to_zipfile(dict,id,family)

@app.route('/get_radar_chart_image/')
def get_radar_chart_image():
    id = id
    family = family
    dict = user_level
    return from_dict_to_radar_chart_displayed(dict,id,family)

@app.route('/get_best_profile/')
def get_best_profile():
    dict = target_comparison 
    return best_profile(dict)

@app.route('/download/')
def download():
    id = id
    return download_file(id)

if __name__=='__main__':
    app.run(port=5000, debug=True)