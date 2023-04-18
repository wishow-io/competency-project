
from flask import Flask, request
import os
from functions import *




#creating folder images
if not os.path.exists("images"):
    os.mkdir("images")



#app
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return 'hello from server'

@app.route('/get_zip_by_user/')
def get_radar_chart_by_family():
    return from_dict_to_zipfile()

@app.route('/get_radar_chart_image/')
def get_radar_chart():
    return from_dict_to_radar_chart_displayed()

@app.route('/get_best_profile/')
def get_best_profile():
    return best_profile()

@app.route('/download/')
def download():
    return download_file()

if __name__=='__main__':
    app.run(port=5000, debug=True)