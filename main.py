import json
from fetcher import fetch_set_cards
from fetcher import dump_json
from fetcher import read_oracle

# dump_json(fetch_set_cards("sum"), "summer_magic")
f=open("summer_magic.json")
data = json.load(f)
dump_json(read_oracle(data), "summer_magic_oracle")