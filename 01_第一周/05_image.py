import requests
import os
root = "C:/Users/ncutz/Documents/code/python/北理mooc/pic/"
url = "https://i0.hdslb.com/bfs/article/7d5ae1cba5b668982a28cf5db8e84ca94ab84ae8.jpg@1320w_1860h.webp"
path = root + "0{}.jpeg"  # url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)

        with open(path.format("b"), 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")




