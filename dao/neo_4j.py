from py2neo import Graph, Node, Relationship
from util import get_book_info

graph = Graph("http://localhost:7474", username="neo4j", password="a8823795")


# 小说 作者 名字 链接
def get_novel_info():
    match_str = 'MATCH (p:novel) return p.author as author,p.name as name,p.href as href,p.imgurl as imgurl limit 5'
    items = graph.run(match_str).data()
    info = get_detail(items)
    for i in range(len(info)):
        book_info = get_book_info.get_data(info[i]['href'])
        info[i]['imgurl'] = book_info[0][5]
    return info


# 获取小说详细信息
def get_novel_detail_info(name, author):
    match_str = 'MATCH (n:novel {name:"' + name + '",author:"' + author + '"}) RETURN n.href as href'
    items = graph.run(match_str).data()
    content = get_book_info.book_detail_info(items[0]['href'])
    return content
# 小说 内容
def get_novel_content(name, author):
    match_str = 'MATCH (n:novel {name:"' + name + '",author:"' + author + '"}) RETURN n.href as href'
    items = graph.run(match_str).data()
    content = get_book_info.book_chapter(items[0]['href'])
    # print(content)
    return content

# 2.数据模型的实现
#创建的几个字段，标题，作者，分类，图片，介绍。
# 通过小说名字或者作者查询小说
def get_novel(text):
    match_str = 'MATCH (p:novel) where p.name=~ ".*' + text + '.*" or p.author=~".*' + text + '.*" return p.author as author,p.name as name,p.type as type,p.imgurl as imgurl,p.intrduce as intrduce,p.href as href limit 20'
    items = graph.run(match_str).data()
    content = get_detail(items)
    print(content)
    return content


# 数据类型转换
def get_detail(items):
    novel_info = []
    for item in items:
        novel_info.append(item)
    # print(novel_info)
    return novel_info


def felei(type):
    match_str = 'MATCH (:type {name:"' + type + '"})-[:novel_type]->(p:novel) RETURN p.author as author,p.name as name,p.href as href,p.imgurl as imgurl limit 5'
    items = graph.run(match_str).data()
    info = get_detail(items)
    for i in range(len(info)):
        book_info = get_book_info.get_data(info[i]['href'])
        print(book_info)
        info[i]['imgurl'] = book_info[0][5]
    return info
