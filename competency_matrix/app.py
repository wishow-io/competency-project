import plotly.express as px
import pandas as pd
from flask import Flask, send_file
import os
import zipfile

#creating folder images
if not os.path.exists("images"):
    os.mkdir("images")

#app
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return 'hello from server'


#save jpeg of the radar chart in zipfile
def generate_zipfile_by_family():
#mock
    dict = {
    "1": {
    
        "Debugging & Observability": {
            "Debugging":"1",
            "Observability":"4"
        },

        "Quality & testing": {
            "écriture de code":"4",
            "testing":"3"
        },

        "Software design & architecure ": {
            "understanding code":"2"
        },
    },

    "2": {

        "Debugging & Observability": {
            "Debugging":"3",
            "Observability":"5"
        },

        "Quality & testing":{
            "écriture de code":"3",
            "testing":"2"
        },

        "Software design & architecure ": {
        "understanding code":"2"
        },
    }
}
    for i in dict:
        with zipfile.ZipFile(f'myzipfile{i}.zip', 'w') as zip_file:
            for j in dict[i]:
                dict[i][j] = {
                    "values": list(dict[i][j].values()),
                    "keys":list(dict[i][j].keys())
                    }  
                print(dict[i][j]) 
                df = pd.DataFrame(dict[i][j])
                fig = px.line_polar(df,r="values",theta="keys",line_close=True)
                fig.update_layout(title=f'Radar de {i} pour {j}')
                fig.write_image(f'images/radar_{i} {j}.jpeg')
                if not os.path.exists(f'myzipfile{i}'):
                    zip_file.write(f'images/radar_{i} {j}.jpeg')
                    os.remove(f'images/radar_{i} {j}.jpeg')
    return "Zip file created"



def generate_radar_chart_image():
    input_dict = {
        "Debugging": 1,
        "Observability": 4,
        "écriture de code": 3,
        "testing": 2,
        "understanding code": 2
    }

    # Normalize input_dict values to range 0-5
    max_val = max(input_dict.values())
    normalized_dict = {k: v / max_val * 5 for k, v in input_dict.items()}

    # Convert the dictionary to the format expected by px.line_polar
    data = {
        "values": list(normalized_dict.values()),
        "keys": list(normalized_dict.keys())
    }
    df = pd.DataFrame(data)

    # Generate the radar chart
    fig = px.line_polar(df, range_r=[0, 5], r="values", theta="keys", line_close=True)
    fig.update_traces(fill='toself')
    fig.write_image('images/radar_chart.jpeg')
    filename = 'images/radar_chart.jpeg'
    return send_file(filename, mimetype='image/jpeg')


@app.route('/get_zip_by_skills_family/')
def get_radar_chart_by_family():
    return generate_zipfile_by_family()

@app.route('/get_radar_chart_image/')
def get_radar_chart():
    return generate_radar_chart_image()


if __name__=='__main__':
    app.run(port=5000, debug=True)