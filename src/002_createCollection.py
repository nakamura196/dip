import requests
from bs4 import BeautifulSoup
import os
import csv
import json

map = {}

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        id = row[0]
        label1 = row[1]
        url = row[2]
        label2 = row[3]

        if id not in map:
            map[id] = {
                "label" : label1,
                "manifests" : []
            }

        map[id]["manifests"].append({
            "@id" : url,
            "label" : label2.strip()
        })


collections = []

for id in map:
    collections.append({
        "@id" : "https://nakamura196.github.io/dip/" + id + ".json",
        "@type" : "sc:Collection",
        "manifests" : map[id]["manifests"],
        "label" : map[id]["label"]
    })

top = {
    "@context" : "http://iiif.io/api/presentation/2/context.json",
    "@id" : "https://nakamura196.github.io/dip/top.json",
    "@type" : "sc:Collection",
    "label" : "Digital Image Publisher",
    "description" : "東京大学史料編纂所・出版物",
    "collections" : collections
}

fw2 = open("../docs/top.json", 'w')
json.dump(top, fw2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

