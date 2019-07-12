import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
# print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
print(soup.title)
print(soup.a.name, soup.a.parent.name)
tag = soup.a
print(tag)
print(tag.attrs)
print(type(tag))

newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")


