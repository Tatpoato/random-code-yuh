import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)

will = input("Do you want to hear a joke (yes/no):  ").lower()

if will == "yes":
    if response.ok:

        data = response.json()

        print(data["joke"])
elif will == "no":
    print("D:")
else:
    print("huh")
