import requests



def getdadjoke():
    url = "https://icanhazdadjoke.com/"

    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(data["joke"])
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")


def getbbquote():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()


        data = data[0]

        quote = data["quote"]
        author = data["author"]
        print(quote)
        print(f"-{author}")
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")


def getchuckjoke():
    url = "https://api.chucknorris.io/jokes/random"

    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(data["value"])
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")



def gettechyboring():
    url = "https://techy-api.vercel.app/api/json"

    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(data["message"])
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")

def getmeowfacts():
    url = "https://meowfacts.herokuapp.com/"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        acdata = data["data"]
        acdata = str(acdata)
        acdata = acdata.replace("[", "").replace("]", "").replace("'", "")
        print(acdata)
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")

def getspacefacts(celobj): #celobj is either sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune or moon
    url = "https://api.bootprint.space/all/"

    realurl = f"{url}{celobj}"

    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(realurl, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data["fact"])
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")


#spacefacts("earth")

def getevilinsult():
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

    headers = {
        "Accept" : "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data["insult"])
        author = data["createdby"]
        if author != "":
            print(f"- {author}")
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")

def getindianquotes():
    url = "https://indian-quotes-api.vercel.app/api/quotes/random"

    headers = {
        "Accept" : "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        print(data["quote"])

        author = data["author"]
        realauthor = author["name"]
        if realauthor != "":
            print(f"- {realauthor}")
    else:
        print(f"Something went wrong: Error Code: {response.status_code}")


# Examples:
# getevilinsult()
# gettechyboring()
# getmeowfacts()
# getbbquote()
# getdadjoke()
# getindianquotes()
# getchuckjoke()
# getspacefacts("earth")
