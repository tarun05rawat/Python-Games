import requests
from datetime import datetime

USERNAME = "tarunrawat"
TOKEN = "uhiihhjj23399999"
GRAPH_ID = "graphtarunrawat"

current_date = datetime.now()




pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
  "id": "graphtarunrawat",
  "name": "Cycling Graph",
  "unit": "Km",
  "type": "float",
  "color": "ajisai",
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
  "date": current_date.strftime("%Y%m%d"),
  "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date.strftime('%Y%m%d')}"
update_pixel_params = {
  "quantity": "50",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date.strftime('%Y%m%d')}"
delete_pixel_params = {
}

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)

