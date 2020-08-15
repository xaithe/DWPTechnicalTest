from flask import Flask, jsonify, request
import bpdts_integration as bpdts
import geocoding

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "<h1>DWP Tech Test API</h1><p>This  is an API for the DWP technical test</p>"

@app.route('/london', methods=['GET'])
def get_users_in_london():
    return jsonify(bpdts.get_city_users("London"))

@app.route('/radius', methods=['GET'])
def get_users_in_radius():
    user_list = bpdts.get_users()
    
    if "miles" in request.args:
        try:
            miles = float(request.args["miles"])
        except ValueError:
            return "Error: miles must be a valid float"
    else:
        miles = 50

    return jsonify(geocoding.users_in_radius(user_list, miles))

if __name__ == '__main__':
    app.run(debug=True)