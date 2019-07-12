import requests
import re
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

# 打印文档中标签为'a'的
print(soup.find_all('a'))
print(soup.find_all(['a', 'b']))
# 打印文档中所有标签名称
for tag in soup.find_all(True):
    print(tag.name)
# 打印文档中带有'course'属性的p标签
print(soup.find_all('p', 'course'))
# 打印文档中属性 id='link1'的元素
print(soup.find_all(id='link1'))
print(soup.find_all(id='link'))
# 使用正则表达式查找
print(soup.find_all(id=re.compile('link')))

'''对比是否查找子孙'''
# 因为a标签是soup下的孙子，所以找不到
print(soup.find_all('a'))
print(soup.find_all('a', recursive=False))
# 因为html标签是soup下的儿子，所以可以找到
print(soup.find_all('html', recursive=False))

# 查找字符串
print(soup.find_all(string='Basic Python'))     # 完全匹配
print(soup.find_all(string=re.compile('python')))  # 正则表达式匹配
