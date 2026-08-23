import requests
import os
from pathlib import Path
from dotenv import load_dotenv

ENV_FILE = Path(__file__).with_name(".env")

load_dotenv(ENV_FILE)

user_params = {
    "token": os.getenv("TOKEN"),
    "username": os.getenv("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=ENDPOINT, json=user_params)

# print(response.text)


graph_endpoint = f"{os.getenv("ENDPOINT")}/{user_params['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": os.getenv("TOKEN"),
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

print("https://pixe.la/v1/users/mik3si7va/graphs/graph1.html")


DATE = "20260823"
QTT = "7"

import datetime

today = datetime.datetime.now().strftime("%Y%m%d")

DATE = today

graph_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

pixel_config = {
    "date": DATE,
    "quantity": QTT,
}

# response = requests.post(url=graph_pixel_endpoint, json=pixel_config, headers=headers)

# print(response.text)

update_pixel_endpoint = f"{graph_pixel_endpoint}/{DATE}"
new_pixel_config = {
    "quantity": "10",
}

# reposse = requests.put(
#     url=update_pixel_endpoint, json=new_pixel_config, headers=headers
# )

# print(reposse.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)

print(response.text)
