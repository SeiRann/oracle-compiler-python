import requests
import json

def dump_json(data, file_name):
    with open(file_name+".json", "w") as f:
        json.dump(data,f)







def fetch_set_cards(set):
    url = "https://api.scryfall.com/cards/search?q=set:lrw"

    headers = {
        "Accept":"application/json",
        "User-Agent":"Test v0.1"
    }

    response = requests.get(url, headers=headers)

    return response.json()