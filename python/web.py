import requests
import csv

###URLの定義　yahoo
url = 'https://news.yahoo.co.jp'

###yahooからデータ取得
req = requests.get(url)

###データを表示する
##for key, value in req.headers.items():
##    print(key, value)

###pathの定義
path = './headers.csv'

###データを表示する
with open(path, 'w') as f:
    reader = csv.reader(f)
    for key, value in req.headers.items():
        print(key, value)