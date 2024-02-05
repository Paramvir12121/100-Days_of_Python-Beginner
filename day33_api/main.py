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
def is_night():
    sunrise = float(data["results"]["sunrise"])
    sunset = float(data["results"]["sunset"])

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour  = int(sunset.split("T")[1].split(":")[0])
    print(sunrise_hour)
    print(sunset_hour)

    time_now = datetime.now()
    hour_now = time_now.hour
    print(hour_now)
    if sunrise_hour <= hour



# Check if your position is in +5 to -5 of long and lat
def is_iss_close():
    if my_lat-5 <= iss_lat <= my_lat+5 and my_longitute-5 <= iss_lng <= my_longitute+5:
        return True

