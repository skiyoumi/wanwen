import py2neo
from py2neo import Graph,Node,Relationship,PropertyDict


##连接neo4j数据库，输入地址、用户名、密码
graph = Graph(
    "http://192.168.1.141:7474",
    username="neo4j",
    password="111111"
)

#创建章节节点
chapter_node=Node(label="chapter", name="第一章")
# 创建属性
chapter_node['href'] ="9154805.html"
graph.create(chapter_node)

#创建书籍节点
book_node=Node(label="book", name="元尊")
graph.create(book_node)
# 创建属性
book_node['content'] ="元尊"
node=Relationship(book_node,'章节',chapter_node)
graph.create(node)
