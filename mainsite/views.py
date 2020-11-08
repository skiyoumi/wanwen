from django.shortcuts import render, HttpResponse, redirect, reverse
from dao import neo_4j
import math
from util import matring
import json


# Create your views here.
def index(request):
    type_name = request.GET.get("type")

    list = neo_4j.get_novel_info()
    if type_name == None:
        type_list = neo_4j.felei("玄幻小说")
    else:
        type_list = neo_4j.felei(type_name)
    return render(request, "index.html", {'data': list, 'type_data': type_list})


# 跳转到小说详情页面
def to_detail(request):
    name = request.GET.get("name")
    author = request.GET.get("author")
    list = neo_4j.get_novel_content(name, author)
    data = matring.list_split(list, 3)
    detail = neo_4j.get_novel_detail(name, author)
    return render(request, "detail.html", {'data': data, 'novel': detail[0]})


# def fenlei(request):
#     type_name=request.GET.get("type")
#     list = neo_4j.get_novel_info()
#     type_list = result = neo_4j.felei(type_name)
#     return render(request, "index.html", {'data': list, 'type_data': type_list})

def search(request):
    search_text = request.GET.get("wd")
    print(search_text)
    if search_text == '':
        return redirect("/")
    else:
        result = neo_4j.get_novel(search_text)
        return render(request, "search.html", {'data': result})


def get_chapter(request):
    # name=凡人修仙传&author=忘语
    name = request.GET.get("name")
    author = request.GET.get("author")
    data = neo_4j.get_nnovel_chapter(name=name, author=author)
    body = matring.list_split(data, 3)
    detail = neo_4j.get_novel_detail(name, author)
    return render(request, "detail.html", {'data': body,'novel': detail[0]})
