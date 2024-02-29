import requests
from dotenv import load_dotenv
import os

pixela_endpoint = "https://pixe.la/v1/users"
load_dotenv()
token = os.getenv('TOKEN')

parameters = {
    "token": token,
    "username": "param12121",
    "agreeTermsOfService":"yes", 
    "notMinor":"yes",
}
# Code to create a user, needed one time 
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.json())

graph_endpoint = f"{pixela_endpoint}/{parameters['username']}/graphs"
print(graph_endpoint)

graph_config = {
    "id":"graph2",
    "name":"Daily Lessons",
    "unit":"pomodoro per day",
    "type":"int",
    "color":"shibafu",
    "timezone":"America/Toronto",
    "isSecret":False,
    "publishOptionalData":False,
}

headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.json())
