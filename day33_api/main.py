import requests
from datetime import datetime
#  need to install package called requests (usually, it worked for me)

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raiseing excption with requests module
response.raise_for_status()

iss_lat = response.json()["iss_position"]["latitude"]
iss_lng = response.json()["iss_position"]["longitude"]

print(iss_lat)
print(iss_lng)

my_lat = 43.653225
my_longitute = -79.383186

parameters = {
    "lat": my_lat,
    "lng": my_longitute,
    "formatted": 0,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour  = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)

