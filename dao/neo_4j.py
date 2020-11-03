from py2neo import Graph, Node, Relationship

graph = Graph("http://localhost:7474", username="neo4j", password="Xc200215")

# 小说 作者 名字 链接
def get_novel_info():
    match_str = 'MATCH (p:novel) return p.author as author,p.name as name,p.href as href,p.imgurl as imgurl limit 5'
    items = graph.run(match_str).data()
    info = get_detail(items)
    return info


# 小说 内容
def get_novel_content(name, author):
    match_str = 'MATCH (n:novel {name:"' + name + '",author:"' + author + '"})-[r:novel_chapter]->(c:chapter) RETURN c.chapterurl as chapterurl,c.name as chapterName'
    items = graph.run(match_str).data()
    content = get_detail(items)
    return content

# 通过小说名字或者作者查询小说
def get_novel(text):
    match_str = 'MATCH (p:novel) where p.name=~ ".*'+text+'.*" or p.author=~".*'+text+'.*" return p.author as author,p.name as name,p.type as type,p.imgurl as imgurl,p.intrduce as intrduce'
    items = graph.run(match_str).data()
    content = get_detail(items)
    return content

# 数据类型转换
def get_detail(items):
    novel_info = []
    for item in items:
        novel_info.append(item)
    # print(novel_info)
    return novel_info

def felei(type):
    match_str = 'MATCH (:type {name:"'+type+'"})-[:novel_type]->(p:novel) RETURN p.author as author,p.name as name,p.href as href,p.imgurl as imgurl limit 5'
    items = graph.run(match_str).data()
    info = get_detail(items)
    return info

# x=get_novel("斗罗大陆")
# print(x)