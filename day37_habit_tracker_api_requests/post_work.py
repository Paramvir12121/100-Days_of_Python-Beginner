import requests
from dotenv import load_dotenv
import os
from datetime import date



pixela_endpoint = "https://pixe.la/v1/users"

load_dotenv()
token = os.getenv('PIXELA_TOKEN')

username = "param12121"
headers = {
    "X-USER-TOKEN": token
}
graph2_endpoint = f"{pixela_endpoint}/{username}/graphs/graph2"

today = date.today()
today = today.strftime("%Y%m%d")
print(today)

pixal_data = {
    "date": today,
    "quantity": "1",
}

response = requests.post(url=graph2_endpoint,json=pixal_data,headers=headers)
print(response.json())