import requests
url = "https://m.so.com/s"
try:
    kw = {"q": "Python"}
    kv = {"user-agent": "Mozilla/5.0"}
    r = requests.get(url, params=kw, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
    with open("360search.html", "w", encoding="utf-8") as f:
        f.write(r.text)
except:
    print("爬取失败")

