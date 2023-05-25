from flask import Flask, request
from flask_cors import CORS, cross_origin

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
    print(locations)
    return {'success':'1'}

if __name__=='__main__':
    app.run(debug=True, port=5002)