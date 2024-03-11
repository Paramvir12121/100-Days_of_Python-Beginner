import random, time, requests


def guess(user_name):
    params = {
        "name": user_name
    }
    response = requests.get("https://api.genderize.io",params=params)
    print(response.json()["gender"])



guess("harry")