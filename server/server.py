from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/api/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        BHK = int(request.form['BHK'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, BHK, bath)
        
        response = jsonify({
            'estimated_price': estimated_price,
            'status': 'success'
        })
        return response
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction....")
    util.load_saved_artifacts()
    app.run()