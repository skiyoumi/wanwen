from util import request
from bs4 import BeautifulSoup
import re


# 获取书籍信息
def get_data(url):
    response = request.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pattern = re.compile(
        '<h1>(.*?)</h1>.*?者:(.*?)</p>.*?别:(.*?)</p>.*?新:<a href=".*?">(.*?)</a></p>.*?<div id="intro">.*?<p>(.*?)</p>.*?<img.*? src="(.*?)"',
        re.S)
    novel_info = re.findall(pattern, str(soup))
    return novel_info


def book_chapter(mach_url):
    resp = request.get(mach_url)
    soup = BeautifulSoup(resp.text, "html.parser")
    chapter_pattern = re.compile('<dd><a href="(.*?)" title="(.*?)">', re.S)
    chapter_info = re.findall(chapter_pattern, str(soup))
    data_list = []
    for item in chapter_info:
        data = {'href': mach_url+item[0], 'chapterName': item[1]}
        data_list.append(data)
    return data_list


def book_detail_info(url):
    resp = request.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    pattern = re.compile(
        '<h1>(.*?)</h1>.*?者:(.*?)</p>.*?别:(.*?)</p>.*?新:<a href=".*?">(.*?)</a></p>.*?<div id="intro">.*?<p>(.*?)</p>.*?<img.*? src="(.*?)"',
        re.S)
    novel_info = re.findall(pattern, str(soup))
    data_list = []
    data = {'imgurl': novel_info[0][5], 'name': novel_info[0][0], 'author': novel_info[0][1], 'type': novel_info[0][2],
            'newest': novel_info[0][3], 'intrduce': novel_info[0][4]}
    data_list.append(data)
    return data_list
