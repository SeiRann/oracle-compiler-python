import json
from fetcher import fetch_set_cards
from fetcher import dump_json
from fetcher import read_oracle
from fetcher import tokenize_strings
from fetcher import split_string


# dump_json(fetch_set_cards("sum"), "summer_magic")
oracle_file=open("summer_magic_oracle.json")
oracle_strings = json.load(oracle_file)

dump_json(tokenize_strings(oracle_strings), "summer_magic_tokanized")

# string = "Enchant creature\nEnchanted creature gets +3/+3.\nAt the beginning of the upkeep of enchanted creature's controller, put a -1/-1 counter on that creature."

# print(split_string(string))