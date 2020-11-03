import requests
from bs4 import BeautifulSoup
import re
import py2neo
from py2neo import Graph,Node,Relationship,PropertyDict
import charpter_text
import time
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="a8823795"
)

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
proxy={'http':'27.157.76.202:4226','http':'182.101.241.28:4251','http':'114.99.222.200:4278','http':'49.82.253.90:4258','http':'122.242.83.193:4234'}
#获取网页资源
def get_html(url):
    while 1<5:
        try:
            response=requests.get(url,headers=header,timeout=(3,7))
            response.encoding = "UTF-8"
            if response.status_code==200:
                return response.text
            else:
                print("false")
                time.sleep(3)
        except:
            print("书籍获取错误重新获取")
            time.sleep(10)
#获取书籍信息和章节
def book_info(soup,mach_url):
    pattern = re.compile(
        '<h1>(.*?)</h1>.*?者:(.*?)</p>.*?别:(.*?)</p>.*?新:<a href=".*?">(.*?)</a></p>.*?<div id="intro">.*?<p>(.*?)</p>.*?<img.*? src="(.*?)"',
        re.S)
    novel_info = re.findall(pattern, str(soup))
    chapter_pattern = re.compile('<dd><a href="(.*?)" title="(.*?)">', re.S)
    chapter_info = re.findall(chapter_pattern, str(soup))
    if len(novel_info) == 0:
        pattern = re.compile(
            '<h1>(.*?)</h1>.*?者:(.*?)</p>.*?别:(.*?)</p>.*?新:<a href=".*?">(.*?)</a></p>.*?<div id="intro"><p>.*?</p>.*?<p>(.*?)</p>.*?<img.*? src="(.*?)"',
            re.S)
        novel_info = re.findall(pattern, str(soup))
    for items in novel_info:
        print(str(novel_info))
        # 查询书籍节点
        book_node = graph.nodes.match("novel", name=items[0]).first()
        # 判断书籍节点是否存在
        if book_node == None:
            # 不存在则创建书籍节点，同时与书籍类别建立连接
            book = Node("novel", name=items[0])
            book['author'] = items[1]
            book['href'] = mach_url
            book['type'] = items[2]
            book['imgurl'] = items[5]
            book['intrduce'] = items[4]
            type_node = graph.nodes.match("type", name=items[2]).first()
            # 判断书籍类型是否存在
            if type_node == None:
                print("书籍类别不存在")
            else:
                novel_type_node = Relationship(type_node, 'novel_type', book)
                graph.create(novel_type_node)
                # 重新获取书籍节点
                book_node = graph.nodes.match("novel", name=items[0]).first()
        else:
            # 创建属性
            book_node['author'] = items[1]
            book_node['type'] = items[2]
            book_node['imgurl'] = items[5]
            book_node['intrduce'] = items[4]
            graph.push(book_node)
        for item in chapter_info:
            # time.sleep(3)
            # 创建章节节点
            chapter_node = Node("chapter", name=item[1])
            # 创建属性
            chapter_node['chapterurl'] = item[0]
            graph.create(chapter_node)
            node = Relationship(book_node, 'novel_chapter', chapter_node)
            graph.create(node)
            print(item[1])
            #获取章节内容
            content = chapter_content(mach_url + item[0])
            #创建章节内容节点
            content_node = Node('charpter_content', name=content)
            graph.create(content_node)
            #建立章节和内容的关系
            chapter_content_node = Relationship(chapter_node, 'chapter_content', content_node)
            graph.create(chapter_content_node)





#获取章节内容
def chapter_content(url_detail):
    chapter_content =charpter_text.get_text(url_detail)
    return chapter_content




def main():
    match_url="MATCH (n:novel) RETURN n.href as href SKIP 0 LIMIT 4450"
    urls=graph.run(match_url).data()
    for item in urls:
        url=item['href']
        print(url)
        html = get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        book_info(soup,url)


if  __name__=="__main__":
    main()
