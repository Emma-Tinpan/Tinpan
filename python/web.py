import requests

###URLの定義　yahoo
url = 'https://news.yahoo.co.jp'

###yahooからデータ取得
req = requests.get(url)

###データを表示する
for key, value in req.headers.items():
    print(key, value)