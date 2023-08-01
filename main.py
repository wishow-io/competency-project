
from dotenv import load_dotenv
from flask import Flask, request
from api.data_functions import *
import os
import hashlib
from api.mock_data.user_score import target_comparison


app = Flask(__name__, template_folder='templates')


load_dotenv()
APP_HOST = os.getenv("HOST")
APP_PORT = os.getenv("PORT")


@app.route('/')
def home():
    return 'hello from server'


@app.route('/get_zip_by_user', methods=['POST'])
def get_zip_by_user():
    data_dict = request.json
    id = hashlib.md5(request.data).hexdigest()
    return from_dict_to_zipfile(data_dict, id)


@app.route('/get_radar_chart_image', methods=['POST'])
def get_radar_chart_image():
    data_dict = request.json
    id = hashlib.md5(request.data).hexdigest()
    return from_dict_to_radar_chart_displayed(data_dict, id)


@app.route('/get_best_profile', methods=['POST'])
def get_best_profile():
    dict = request.json
    return best_profile(dict)


if __name__ == '__main__':
    app.run(port=APP_PORT, host=APP_HOST, debug=True)
