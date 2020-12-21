import requests
from bs4 import BeautifulSoup
import os
import csv

# スクレイピング対象のhtmlファイルからsoupを作成
soup = BeautifulSoup(open('data/index1.htm'), 'html.parser')

aas = soup.find_all("a")

rows = []
rows.append(["url1", "label1", "url2", "label2"])

for aa in aas:
    label = aa.text
    
    # path = "data/p"+aa.get("href").split("./")[1]
    path3 = "data/"+aa.get("href").split("./")[1]

    label0 = path3.split("data/")[1].split(".")[0]

    soup3 = BeautifulSoup(open(path3), 'html.parser')

    ifr = soup3.find("iframe")

    if not ifr:
        print(path3)
        continue

    path = "data/"+ifr.get("src")

    # print(path)

    

    if os.path.exists(path):

        # スクレイピング対象のhtmlファイルからsoupを作成
        soup2 = BeautifulSoup(open(path), 'html.parser')

        options = soup2.find_all("option")

        for option in options:
            # print(option)

            url = option.get("value")

            if "hi.u-tokyo.ac.jp" in url:
                # print(url, option.text)

                rows.append([label0, label, url, option.text])
    
    else:
        print("not", path)



with open('data.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)
