import requests
from bs4 import BeautifulSoup
import os
import csv
import json

map = {}
map2 = {}

with open('data2.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        id = row[0]
        label1 = row[1]
        url = row[2]
        label2 = row[3]

        label0 = row[4]
        if label0 not in map2:
            map2[label0] = {}

        if id not in map2[label0]:
            map2[label0][id] = {
                "label" : label1,
                "manifests" : []
            }

        map2[label0][id]["manifests"].append({
            "@id" : url,
            "label" : label2.strip()
        })


collections = []

for label0 in map2:

    map = map2[label0]

    collections2 = []

    for id in map:
        collections2.append({
            "@id" : "https://nakamura196.github.io/dip/" + id + ".json",
            "@type" : "sc:Collection",
            "manifests" : map[id]["manifests"],
            "label" : map[id]["label"]
        })

    coll = {
        "label" : label0,
        "@id" : "https://nakamura196.github.io/dip/"+label0+".json",
        "@type" : "sc:Collection",
        "collections" : collections2
    }

    collections.append(coll)

top = {
    "@context" : "http://iiif.io/api/presentation/2/context.json",
    "@id" : "https://nakamura196.github.io/dip/top.json",
    "@type" : "sc:Collection",
    "label" : "Digital Image Publisher",
    "description" : "東京大学史料編纂所・出版物",
    "collections" : collections,
    "vhint" : "flat"
}

fw2 = open("../docs/top.json", 'w')
json.dump(top, fw2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

