from flask import Flask, render_template, jsonify, request
import joblib
import os
from areasDicts import areasForWork
import pandas as pd
import numpy as np

data_dir = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(data_dir, 'FINAL_DATASET_643.csv')

df = pd.read_csv(data_file)

app = Flask(__name__)

model_path = os.path.join(app.root_path, 'model.joblib')

model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html', name='Testing template')

@app.route('/getPredicts', methods=['GET'])
def getPredicts():
    doneAreas = []
    id = request.args.get('id', default = 1)
    for i in range(len(areasForWork)):
        areasForWork[i]['predict'] = []
        areasForWork[i]['predict'].append(model.predict([areasForWork[i]['predictParams'][int(id) - 1]]).tolist())
        X = df[df['Район'] == areasForWork[i]['meteo']]
        X = X.drop(['Проиcшествие','Дата','Район'], axis=1)
        sr = model.predict(X).mean()
        areasForWork[i]['predict'].append(sr)
    return jsonify(areasForWork)
