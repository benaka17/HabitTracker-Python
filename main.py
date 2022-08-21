from datetime import datetime
import requests

"""
Link(s):
https://docs.pixe.la/
https://pixe.la/v1/users/alexanderb/graphs/graph1.html
"""

pixela_endpoint = "https://pixe.la/v1/users"

# Constants
USERNAME = "alexanderb"
TOKEN = "aldkgknvi879873qfmn3"
GRAPH_ID = "graph1"

# Set up the user
userParams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=pixela_endpoint, json=userParams)
#print(response.text)


# Create a new graph on pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphConfig = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "Min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graphConfig, headers=headers)
#print(response.text)


# Create a new pixel, = adding data
pixelCreation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(f"Today's date: {today.strftime('%Y%m%d')}")

pixelData = {
    "date": today.strftime("%Y%m%d"), # yyyyMMdd
    "quantity": "5"
}
#response = requests.post(url=pixelCreation_endpoint, json=pixelData, headers=headers)
#print(response.text)


# Update pixel using put method
changeDate = datetime(year=2022, month=8, day=14).strftime("%Y%m%d")
print(f"Date to be changed: {changeDate}")
pixelUpdate_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{changeDate}"

pixelUpdate = {
    "quantity": "7"
}
#response = requests.put(url=pixelUpdate_endpoint, json=pixelUpdate, headers=headers)
#print(response.text)


# Delete a pixel using the delete method
deleteDate = datetime(year=2022, month=8, day=14).strftime("%Y%m%d")
print(f"Date to be deleted: {deleteDate}")
pixelDelete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{deleteDate}"

response = requests.delete(url=pixelDelete_endpoint, headers=headers)
print(response.text)
