import requests
from bs4 import BeautifulSoup
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

'''下行遍历'''
# 父节点一
print(soup.head)
print(soup.head.contents)   # 子节点

# 父节点二
print(soup.body)
print(soup.body.contents)   # 子节点
print(len(soup.body.contents))  # 子节点的数量
print(soup.body.contents[0])  # 第一个子节点
print(soup.body.contents[1])  # 第二个子节点

# 遍历儿子节点
for child in soup.body.children:
    print(child)

# 遍历子孙节点
for child in soup.body.children:
    print(child)

'''上行遍历'''
print(soup.title.parent)
print(soup.html.parent)  # html的父亲是自身
print(soup.parent)  # soup本身的父亲是None

# 遍历父亲节点
for parent in soup.a.parents:   # 父亲、爷爷、曾祖父.....
    if parent is None:
        print(parent)   # 因为一定会遍历到soup的本身，这个时候它父亲是None，所以打印本身
    else:
        print(parent.name)

'''平行遍历   有条件:平行遍历发生在同一父节点下的各节点间'''
print(soup.a.next_sibling)  # a标签的下一个节点
# 打印出 'and' 说明各个节点间的平行遍历的结果不一定是标签类型，还可能是<class 'bs4.element.NavigableString'>，平行遍历时，需要分情况讨论
print(type(soup.a.next_sibling))
print(soup.a.next_sibling.next_sibling)  # a标签下一个节点的下一个节点
print(soup.a.previous_sibling)  # a表示的前一个节点
print(soup.a.previous_sibling.previous_sibling)

# 遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)
# 遍历前续节点
for sibling in soup.a.previous_siblings:
    print(sibling)
