import requests
import json
import math

# helper function for dumping json files
def dump_json(data, file_name):
    with open(file_name+".json", "w") as f:
        json.dump(data,f)

# fetch function that fetches all of the cards in a set
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


# filter out only the oracle texts from the cards
def read_oracle(data):
    oracle_texts = []

    for card in data:
        oracle_texts.append(f"{card["oracle_text"]}")

    


    return oracle_texts

# ["Turn", "the", "oracle", "text", "into", "tokens"]

def split_string(string: str) -> list:
    string = string.replace("\n", " ")
    tokens = string.split()

    return tokens

def tokenize_strings(strings) -> list:
    tokenized_strings = []

    for string in strings:
        text = split_string(string)
        tokenized_strings.append(text)

    return tokenized_strings

