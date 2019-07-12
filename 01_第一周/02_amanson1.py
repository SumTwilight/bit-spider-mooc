import requests
url = "https://www.amazon.com/dp/B01FJS2MXU/"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
    with open("amazon.html", "w", encoding="utf-8") as f:
        f.write(r.text)
except:
    print("爬取失败")
