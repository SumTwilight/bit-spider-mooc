import requests
from bs4 import BeautifulSoup
import bs4


# 1：从网络上获取大学排名网页内容
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 2：提取网页内容中的信息到合适的数据结构
def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:      # 注意这里不是用的find_all
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])
            '''tds[0] <td>1</td>
               tds[1] <td><div align="left">清华大学</div></td>
               tds[2] <td>北京</td><td>94.6</td>
               tds[3] <td class="hidden-xs need-hidden indicator5">100.0</td>
               ...    <td class="hidden-xs need-hidden indicator6"style="display: none;">98.30%</td>
            '''


# 3：利用数据结构展示并输出结果
def print_univ_list(ulist, num):
    tplt = "{0:^6}{1:{4}^10}{2:{4}^10}{3:<10}"
    print(tplt.format("rank", "学校名称", "地区", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

    '''无法对齐：中西文字符宽度不同
    print("{:6}{:^15}{:^10}{:^10}".format("排名", "学校名称", "地区", "总分"))
        for i in range(num):
            u = ulist[i]
            print("{:6}  {:^15}{:^10}{:^10}".format(u[0], u[1], u[2], u[3]))
    '''


if __name__ == "__main__":
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 20)  # 20 univs
