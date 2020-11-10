from django.shortcuts import render, HttpResponse, redirect, reverse
from dao import neo_4j
from util import matring
from until import novel_content
from util import get_book_info


# Create your views here.

def novel_read(request):
    url = request.GET.get("keyword")
    content = novel_content.read_book(url);
    return render(request, "read.html", {"content": content});


# 首页
def index(request):
    type_name = request.GET.get("type")

    list = neo_4j.get_novel_info()
    if type_name == None:
        return redirect("/?type=玄幻小说")
    else:
        type_list = neo_4j.felei(type_name)
    return render(request, "index.html", {'data': list, 'type_data': type_list})


# 小说详情
def to_detail(request):
    name = request.GET.get("name")
    author = request.GET.get("author")
    list = neo_4j.get_novel_content(name, author)
    data = matring.list_split(list, 3)
    detail = neo_4j.get_novel_detail(name, author)
    return render(request, "detail.html", {'data': data, 'novel': detail[0]})


# 小说搜索
def search(request):
    search_text = request.GET.get("wd")
    # print(search_text)
    if search_text == '':
        return redirect("/")
    else:
        result = neo_4j.get_novel(search_text)
        print(result)
        body = []
        if len(result) > 0:
            body = matring.list_split(result, 6)
        else:
            return render(request, "serach.html", {'err': '没有找到数据'})
        return render(request, "serach.html", {'data': body})


# 小说章节
def get_chapter(request):
    # 小说内容目录跳转
    url = request.GET.get("keyword")
    print(url)
    # name=凡人修仙传&author=忘语
    name = request.GET.get("name")
    author = request.GET.get("author")
    data = neo_4j.get_nnovel_chapter(name=name, author=author)
    body = matring.list_split(data, 3)
    detail = neo_4j.get_novel_detail(name, author)
    print(name)
    if (url == None):
        data = detail[0]
    else:
        list = get_book_info.book_detail_info(url)
        data = list

    return render(request, "detail.html", {'data': body, 'novel': data})


def more(request):
    search_text = request.GET.get("type")
    page = int(request.GET.get("page"))
    # print(search_text)
    if search_text == '':
        return redirect("/")
    else:
        sum = neo_4j.get_type_num(search_text)
        if sum % 30 == 0:
            sum_page = sum / 3
        else:
            sum_page = int(sum / 30) + 1
        if page <= 0:
            return redirect('/more?type=' + search_text + '&page=1')
        elif page > sum_page:
            return redirect('/more?type=' + search_text + '&page=' + sum_page + '')
        result = neo_4j.get_type(search_text, page=page)
        if len(result) > 0:
            body = matring.list_split(result, 6)
        else:
            return render(request, "more.html", {'err': '没有找到数据'})
        if page < 5:
            page_item = range(1, page + 5)
        elif page >= 5 and page < sum_page - 5:
            page_item = range(page - 4, page + 5)
        elif page > 5 and page >= sum_page - 5:
            page_item = range(page - 5, sum_page + 1)
        # for i in :
        #     page.append(i)
        return render(request, "more.html", {'data': body, 'sum': sum_page, 'page': page_item})
