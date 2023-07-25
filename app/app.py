
from dotenv import load_dotenv
from flask import Flask
from data_functions import *
from mock_data.user_score import *
import os


app = Flask(__name__, template_folder='templates')


load_dotenv()
APP_HOST = os.getenv("HOST")
APP_PORT = os.getenv("PORT")


@app.route('/')
def home():
    return 'hello from server'


@app.route('/get_zip_by_user/<int:id>/')
def get_zip_by_user(id):
    data_dict = user_level_by_family
    return from_dict_to_zipfile(data_dict, id)


@app.route('/get_radar_chart_image/<int:id>/')
def get_radar_chart_image(id):
    data_dict = user_level
    return from_dict_to_radar_chart_displayed(data_dict, id)


@app.route('/get_best_profile/')
def get_best_profile():
    dict = target_comparison
    return best_profile(dict)


@app.route('/download/<int:id>/<path:filename>')
def download(filename, id):
    return download_file(id, filename)


if __name__ == '__main__':
    app.run(port=APP_PORT, host=APP_HOST, debug=True)
