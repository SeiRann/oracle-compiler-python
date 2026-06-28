import requests
import json
import math

def dump_json(data, file_name):
    with open(file_name+".json", "w") as f:
        json.dump(data,f)

def fetch_set_cards(set):
    data = []
    url = "https://api.scryfall.com/cards/search?q=set:"+set

    headers = {
        "Accept":"application/json",
        "User-Agent":"Test v0.1"
    }

    response = requests.get(url, headers=headers)

    data.extend(response.json()["data"])
    total_cards = int(response.json()["total_cards"])
    response_data = response.json()

    if total_cards>175 :
        for i in range(math.ceil(total_cards/175)-1):
            next_url = response_data["next_page"]

            response = requests.get(next_url,headers=headers)

            response_data = response.json()
            data.extend(response_data["data"])


    return data

def read_oracle(data):
    oracle_texts = []

    for card in data:
        oracle_texts.append(f"{card["oracle_text"]}")

    


    return oracle_texts

def tokenize_string(string):
    tokens = []
    temp_token = ""


    for character in string:
        if character != " ":
            temp_token+= character
        elif character == " " and temp_token != "":
            tokens.append(temp_token)
            temp_token = ""

    return tokens
