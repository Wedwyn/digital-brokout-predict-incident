from flask import Flask, render_template, jsonify, request
import joblib
import os


app = Flask(__name__)

model_path = os.path.join(app.root_path, 'RandomForrestRegressor.joblib')

model = joblib.load(model_path)

# model = joblib.load('./RandomForrestRegresssor.joblib')

# @app.route('/')
# def hello_world():
#   return render_template('index.html', 'name'='Testing template')

areas = [{ 'name': 'Краснокамский городской округ', 'predict': 0 },
         { 'name': 'Пермский муниципальный округ', 'predict': 0 },
   { 'name': 'Пермский городской округ', 'predict': 0 },
   { 'name': 'Соликамский городской округ', 'predict': 0 },
   { 'name': 'Кунгурский муниципальный округ', 'predict': 0 },
   { 'name': 'городской округ Березники', 'predict': 0 },
   { 'name': 'Суксунский городской округ', 'predict': 0 },
   { 'name': 'Чайковский городской округ', 'predict': 0 },
   { 'name': 'Чусовской городской округ', 'predict': 0 },
   { 'name': 'Лысьвенский городской округ', 'predict': 0 }
]

@app.route('/')
def index():
    return render_template('index.html', name='Testing template')

@app.route('/getPredicts', methods=['GET'])
def getPredicts():
    # Получаем параметром день на который мы делаем прогноз
    id = request.args.get('id', default = 0)
    if id == '4':
        for i in range(len(areas)):
            areas[i]['predict'] = model.predict([[ 0.77227066, -1.28162094, -0.26821334, -0.30143562,  1.06333304,
            0.69093134,  0.01698846,  0.06093193,  1.52417853, -0.1842971 ,
            -0.26809819, -0.23811762, -0.17520988, -1.01086025]]).tolist()
    else:
        for i in range(len(areas) - 3):
            areas[i]['predict'] = model.predict([[ 0.437227066, -1.56162094, -0.54736821334, 0.30143562,  1.06333304,
            0.69093134,  0.61698846,  0.06093193,  1.52417853, -0.1842971 ,
            -0.26809819, -0.23811762, -0.17520988, -1.01086025]]).tolist()
    return jsonify(areas)


# predictions = model.predict([[ 0.77227066, -1.28162094, -0.26821334, -0.30143562,  1.06333304,
#          0.69093134,  0.01698846,  0.06093193,  1.52417853, -0.1842971 ,
#         -0.26809819, -0.23811762, -0.17520988, -1.01086025], [ 0.77227066, -1.28162094, -0.26821334, -0.30143562,  1.06333304,
#          0.69093134,  0.01698846,  0.06093193,  1.52417853, -0.1842971 ,
#         -0.26809819, -0.23811762, -0.17520988, -1.01086025]])
