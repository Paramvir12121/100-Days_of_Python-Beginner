import requests 
#  need to install package called requests (usually, it worked for me)

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # Raiseing excption with requests module
# response.raise_for_status()

# print(response.content)

# data = response.json()["iss_position"]

# print(data)
my_lat = 43.653225
my_longitute = -79.383186

parameters = {
    "lat": my_lat,
    "lng": my_longitute,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()


print(data["results"]["sunrise"])