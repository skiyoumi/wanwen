import re
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
url = "http://www.biquge.info/10_10582/4410172.html"

# 获取源代码
def get_html(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = "UTF-8";
    if response.status_code == 200:
        html = response.text
        return html
    else:
        print("获取网站源码失败")


def get_content(html):
    parttern = re.compile('<h1>(.*?)</h1>.*?<div id="content"><!--go-->(.*?)<!--over-->', re.S)
    items = re.findall(parttern, html)
    data = {'title': items[0][0], 'content': items[0][1]}
    return data

def read():
    html = get_html(url, headers)
    data=get_content(html)
    print(data)
    return data

