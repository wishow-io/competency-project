
from flask import Flask
from data_functions import *
from mock_data.user_score import *



app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return 'hello from server'


@app.route('/get_zip_by_user/')
def get_zip_by_user():
    data_dict = user_level_by_family
    id = 2
    family= 'test'
    return from_dict_to_zipfile(data_dict, id,family)

@app.route('/get_radar_chart_image/')
def get_radar_chart_image():
    id = 2
    family = "family1"
    data_dict = user_level
    return from_dict_to_radar_chart_displayed(data_dict, id, family)

 
@app.route('/get_best_profile/')
def get_best_profile():
    dict = target_comparison
    return best_profile(dict)


@app.route('/download/')
def download():
    id = 2
    return download_file(id)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
