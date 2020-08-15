from flask import Flask, jsonify, request
import users
import geocoding

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello World!"

@app.route('/london', methods=['GET'])
def get_users_in_london():
    return jsonify(users.get_city_users("London"))

@app.route('/radius', methods=['GET'])
def get_users_in_radius():
    user_list = users.get_users()
    
    if "miles" in request.args:
        miles = int(request.args["miles"])
    else:
        return "Error: No radius provided. Please specify a radius."

    return jsonify(geocoding.users_in_radius(user_list, miles))

if __name__ == '__main__':
    app.run(debug=True)