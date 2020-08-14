import requests

API_URL = "https://bpdts-test-app.herokuapp.com/"
USERS_URL = API_URL + "users"
CITY_URL = API_URL + "city"

def get_users(url):
    req = requests.get(USERS_URL)

    return req.json()