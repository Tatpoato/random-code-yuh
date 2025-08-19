import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

if response.ok:

    data = response.json()

    print(data["joke"])
