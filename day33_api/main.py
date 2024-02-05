import requests 
#  need to install package called requests (usually, it worked for me)

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if response.code != 200:
#     if response.code == 404:
#         raise Exception("This resourse does not exist!")
#     elif response.code == 401:
#         raise Exception("You are not authorised to access this data.")
#     else:
#         print(requests)

# Raiseing excption with requests module
response.raise_for_status()

print(response.content)

data = response.json()["iss_position"]

print(data)