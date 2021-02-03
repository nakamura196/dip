import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request

prefix = "https://nakamura196.github.io/dip/data"

json_open = open("../docs/hi.json", 'r')
df = json.load(json_open)
collections = df["collections"]

for collection in collections:
    filename = collection["@id"].split("/")[-1]

    path = "../docs/" + filename

    collection["@id"] = prefix + "/" + filename

    for collection2 in collection["collections"]:

        filename = collection2["@id"].split("/")[-1]

        path = "../docs/" + filename

        collection2["@id"] = prefix + "/" + filename

        f1 = open(path, 'w')
        json.dump(collection2, f1, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

    f1 = open(path, 'w')
    json.dump(collection, f1, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))