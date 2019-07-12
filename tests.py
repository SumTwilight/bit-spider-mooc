root = "./pic/"
url = "https://i0.hdslb.com/bfs/article/3f24481dfa27185d9fefdeb2639de3cda7555019.jpg@1320w_702h.webp"
path = root + "0{name}.jpeg"  # url.split('/')[-1]
print(type(path))
print(path.format(name="a"))
print(path)