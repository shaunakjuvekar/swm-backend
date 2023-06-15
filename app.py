from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import gurobi as gc
import csv_convert 
import time

app = Flask(__name__)
CORS(app, support_credentials=True)




@app.route('/') 
def hello():
    return '<h1>Hello, World!</h1>'

@app.route("/add", methods=["POST"], strict_slashes=False)
@cross_origin(support_credentials=True)
def add_articles():
    #title = request.json['title']
    #body = request.json['body']
    locations = request.json
    #for tp in locations:
    #    print(tp)
    return {'success':'1'}

@app.route("/send", methods=["POST"], strict_slashes=False)
@cross_origin(support_credentials=True)
def receive_data():
    #title = request.json['title']
    #body = request.json['body']
    locations = request.json
    #gurobi(locations)
    #sleep(120)
    #python run (csv_convert.py)
    #csv_transform.convert_csv(locations)
    print(locations)
    try:
        with open("route_data.py", "w") as json_file:
            json.dump(locations, json_file)
    except:
        print("Error while witing to file")
    finally:
        print("Success")

    gc.main()
    time.sleep(5)
    csv_convert.main()
    
    #exec(gc)
    #runpy.run_path(path_name='gurobi.py')
        
    return {'success':'1'}


@app.route("/get_data", methods=["GET"], strict_slashes=False)
@cross_origin(support_credentials=True)
def send_data():
    #title = request.json['title']
    #body = request.json['body']
    with open("data_file.json", "r") as data:
        route_data = json.load(data)
    print(route_data)
    return route_data

if __name__=='__main__':
    app.run(debug=True, port=5002, use_reloader=False)