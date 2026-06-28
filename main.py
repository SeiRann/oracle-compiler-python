import json
from fetcher import fetch_set_cards
from fetcher import dump_json
from fetcher import read_oracle
from fetcher import tokenize_string

# dump_json(fetch_set_cards("sum"), "summer_magic")
f=open("summer_magic_oracle.json")
data = json.load(f)
print(data[1])
print(tokenize_string(data[1]))