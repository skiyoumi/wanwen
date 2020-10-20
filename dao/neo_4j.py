from py2neo import Graph,Node,Relationship

graph = Graph("http://192.168.1.141:7474", username="neo4j", password="111111")

#小说 作者 名字 链接
def get_novel_info(graph):
    match_str = 'MATCH (p:novel) return p.author as author,p.name as name,p.href as href limit 4'
    items = graph.run(match_str).data()
    info = get_detail(items)
    return info

#小说 内容
def get_novel_content(graph):
    match_str = 'MATCH (n:charpter_content) RETURN n.name as content LIMIT 1'
    items = graph.run(match_str).data()
    content=get_detail(items)
    return content

#数据类型转换
def get_detail(items):
    novel_info = []
    for item in items:
        novel_info.append(item)
    print(novel_info)
    return novel_info

def main():
    # get_novel_content(graph)
    get_novel_info(graph)

if __name__ == '__main__':
    main()


