from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import gurobi as gc
import csv_convert 

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/send", methods=["POST"], strict_slashes=False)
@cross_origin(support_credentials=True)
def receive_data():
    #title = request.json['title']
    #body = request.json['body']
    locations = request.json
    #print(locations)
    try:
        with open("route_data.py", "w") as json_file:
            json.dump(locations, json_file)
            
    except:
        print("Error while writing to file")
    
    finally:
        print("Finally Block")

    gc.main()
    csv_convert.main()
    return {'success':'1'}

@app.route("/get_data", methods=["GET"], strict_slashes=False)
@cross_origin(support_credentials=True)
def send_data():
    try:
        with open("data_file.json", "r") as data:
            route_data = json.load(data)
        print("get_data called")
        return route_data
    except:
        return {"failure":'0'}
    finally:
        print("IN final block")
        #Can delete delete data_file.json in future

if __name__=='__main__':
    app.run(debug=True, port=5002, use_reloader=False)