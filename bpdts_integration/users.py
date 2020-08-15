import requests

API_URL = "https://bpdts-test-app.herokuapp.com/"
USERS_URL = API_URL + "users"
USER_URL = API_URL + "user/"
CITY_URL = API_URL + "city/"

def get_users():
    req = requests.get(USERS_URL)

    return req.json()

def get_user(id):
    uri = USER_URL + str(id)

    req = requests.get(uri)

    return req.json()

def get_city_users(city):
    uri = CITY_URL + city + "/users"

    req = requests.get(uri)

    return req.json()

