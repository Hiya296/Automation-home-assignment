import gettext
from io import BytesIO
import requests
import json
from PIL import Image

DRONES_API_URL = "https://interviews-api.beefreeagro.com/api/v1/drones"
response = requests.get(DRONES_API_URL)
data = json.loads(response.text)
drones_code = []

with open("code.txt", "r") as file:
    inputs = file.readlines()

for text in inputs:
    drones_code.append(text.strip())


def show_all_drones():
    global data
    for i in range(0, len(data)):
        if response.status_code == 200:
            data = json.loads(response.text)[i]
            i += 1
            print(data)
        else:
            print("API request failed. Status code:", response.status_code)


show_all_drones()


def specific_drone():
    global data
    for i in range(len(drones_code)):
        drone_code = gettext.gettext(drones_code[i])
        specific_drone_api = f"https://interviews-api.beefreeagro.com/api/v1/drones/{drone_code}"
        drone_response = requests.get(specific_drone_api)
        if drone_response.status_code == 200:
            drone_data = json.loads(drone_response.text)
            print(drone_data)
        else:
            print("API request failed. Status code:", drone_response.status_code)


specific_drone()


def drone_image():
    global data
    for i in range(len(drones_code)):
        drone_code = gettext.gettext(drones_code[i])
        specific_drone_api = f"https://interviews-api.beefreeagro.com/api/v1/drones/{drone_code}/image"
        drone_response = requests.get(specific_drone_api)
        if drone_response.status_code == 200:
            image_data = drone_response.content
            image_file = BytesIO(image_data)
            image = Image.open(image_file)
            image.show()
        else:
            print("API request failed. Status code:", drone_response.status_code)


drone_image()
