import requests
from datetime import datetime

today = datetime.now()

USERNAME = 'andarwilho'
TOKEN = 'as3d1as6d1ad654a65161asdad'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

user_params = {
    'token': TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor' : 'yes',
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_params = {
    'id' : 'graph1',
    'name' : 'Programming Graph',
    'unit' : 'commit',
    'type' : 'int',
    'color' : 'momiji'
}

graph_headers = {
    'X-USER-TOKEN' : TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=graph_headers)

pixel_params = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : '6',
} 
# POST THE PIXEL IN THE DAY
# response = requests.post(url=f'{GRAPH_ENDPOINT}/graph1', json=pixel_params, headers=graph_headers)

# UPTADE THE DAY PIXEL
# response = requests.put(url=f'{GRAPH_ENDPOINT}/graph1/{today.strftime("%Y%m%d")}', json=pixel_params, headers=graph_headers)

# DELETE THE PIXEL
response = requests.delete(url=f'{GRAPH_ENDPOINT}/graph1/{today.strftime("%Y%m%d")}', headers=graph_headers)
print(response.text)
