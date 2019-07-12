import requests
url = "http://www.baidu.com/s"
try:
    kw = {'wd': 'Python'}
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, params=kw, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
    with open("baidu1.html", "w", encoding="utf-8") as f:
        f.write(r.text)
except:
    print("爬取失败")
