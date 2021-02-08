from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json
import requests
import pandas as pd
import random

app = Flask(_name_)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET','POST'])
def facts():
    data = pd.read_csv('facts.csv')
    facts = list(data['Facts'])
    value=(random.choices(facts))
    #print(type(value[0]))
    data = {
       'fact' : value[0],
    }
    data = json.dumps(data)
    return jsonify(data)

if __name__=='__main__':
    #server = Server(app.wsgi_app)
    #server.serve()
    #server.watch('/Views/*')
    app.run(debug=False)
    #app.config['DEBUG'] = True
    #app.config['TEMPLATES_AUTO_RELOAD'] = True
