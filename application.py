# from flask import Flask, request, jsonify, render_template
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor

# app = Flask(__name__)  # use one consistent app variable

# # Load the trained model
# random_forest = pickle.load(open('models/randomforest.pkl', 'rb'))

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/prediction', methods=['GET', 'POST'])  # fixed typo
# def car_price():
#     if request.method == 'POST':
#         try:
#             model = float(request.form.get('model'))
#             vehicle_age = float(request.form.get('vehicle_age'))
#             km_driven = float(request.form.get('km_driven'))
#             seller_type = float(request.form.get('seller_type'))
#             fuel_type = float(request.form.get('fuel_type'))
#             transmission_type = float(request.form.get('transmission_type'))
#             mileage = float(request.form.get('mileage'))
#             engine = float(request.form.get('engine'))
#             max_power = float(request.form.get('max_power'))
#             seats = float(request.form.get('seats'))

#             prediction = random_forest.predict([[model, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats]])
#             result = round(prediction[0], 2)
#             return render_template('prediction.html', result=result)

#         except Exception as e:
#             return f"Error occurred: {e}"

#     return render_template('prediction.html')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')



from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('models/randomforest.pkl', 'rb') as file:
    random_forest = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        try:
            # Get form inputs
            model = float(request.form['model'])
            vehicle_age = float(request.form['vehicle_age'])
            km_driven = float(request.form['km_driven'])
            seller_type = float(request.form['seller_type'])
            fuel_type = float(request.form['fuel_type'])
            transmission_type = float(request.form['transmission_type'])
            mileage = float(request.form['mileage'])
            engine = float(request.form['engine'])
            max_power = float(request.form['max_power'])
            seats = float(request.form['seats'])

            # Make prediction
            features = [[model, vehicle_age, km_driven, seller_type, fuel_type,
                         transmission_type, mileage, engine, max_power, seats]]
            prediction = random_forest.predict(features)
            result = round(prediction[0], 2)

            return render_template('prediction.html', result=result)

        except Exception as e:
            return f"Error occurred: {e}"

    return render_template('prediction.html', result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
