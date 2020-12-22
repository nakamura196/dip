import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request

url = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/series.json'
res = urllib.request.urlopen(url)
# json_loads() でPythonオブジェクトに変換
data = json.loads(res.read())

collections0 = []

for x in range(len(data)):
    obj = data[x]
    title1 = obj["title"]
    id1=obj["id"]

    print("* "+str(x+1)+"/"+str(len(data))+"="+str(id1))

    url1 = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/'+id1+'.json'

    # sleep(1)

    res1 = urllib.request.urlopen(url1)
    # json_loads() でPythonオブジェクトに変換
    data1 = json.loads(res1.read())

    collections = []

    for y in range(len(data1)):
        obj1 = data1[y]
        title2 = obj1["title"]
        id2 = obj1["id"]

        print("** "+str(y+1)+"/"+str(len(data1))+"="+str(id2))

        url2 = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/'+id1+"-"+id2+'.json'

        # sleep(1)

        res2 = urllib.request.urlopen(url2)
        # json_loads() でPythonオブジェクトに変換
        data2 = json.loads(res2.read())

        manifests = []

        for z in range(len(data2)):
            obj2 = data2[z]
            url3 = obj2["url"]
            no = obj2["no"]
            desc = obj2["description"]

            manifest = {
                "@id" : obj2["url"],
                "label" : obj2["no"] + " " + obj2["description"]
            }

            manifests.append(manifest)

        collection = {
            "@id" : url2,
            "label" : title2,
            "@type" : "sc:Collection",
            "manifests" : manifests
        }

        collections.append(collection)

    collection0 = {
        "@id" : url1,
        "label" : title1,
        "@type" : "sc:Collection",
        "collections" : collections
    }

    collections0.append(collection0)

all = {
    "@context" : "http://iiif.io/api/presentation/2/context.json",
    "@id" : "https://nakamura196.github.io/dip/hi.json",
    "@type" : "sc:Collection",
    "collections" : collections0,
    "label" : "史料集版面ギャラリー",
    "description" : "東京大学史料編纂所により編纂・出版した史料集の版面画像ギャラリーです。 編纂・出版の詳細は<a href='https://www.hi.u-tokyo.ac.jp/publication/publication_top-j.html'>こちら</a>でご確認ください。<br/>クリエイティブ・コモンズ・ライセンスの「CC BY-NC-SA」（<a href='https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja'>クリエイティブ・コモンズ　表示 - 非営利 - 継承 4.0 国際ライセンス</a>）相当の条件で提供しています。詳細は<a href='https://www.hi.u-tokyo.ac.jp/faq/reuse_cc-by-nc-sa.html'>こちら</a>でご確認ください。"
}

f1 = open("../docs/hi.json", 'w')
json.dump(all, f1, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))