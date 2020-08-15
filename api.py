from flask import Flask, jsonify, request
import bpdts_integration as bpdts
import geocoding

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello World!"

@app.route('/london', methods=['GET'])
def get_users_in_london():
    return jsonify(bpdts.get_city_users("London"))

@app.route('/radius', methods=['GET'])
def get_users_in_radius():
    user_list = bpdts.get_users()
    
    if "miles" in request.args:
        miles = int(request.args["miles"])
    else:
        return "Error: No radius provided. Please specify a radius."

    return jsonify(geocoding.users_in_radius(user_list, miles))

if __name__ == '__main__':
    app.run(debug=True)