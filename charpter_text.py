import requests
import re
import time

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
def get_text(url):
    while 1<5:
        try:
            response = requests.get(url, headers=header,timeout=(3,7))
            response.encoding = "UTF-8"
            if response.status_code == 200:
                html = response.text
                try:
                    pattern = re.compile('<div id="content"><!--go-->(.*?)<!--over-->', re.S)
                    text_info= re.findall(pattern, html)
                    # print(text_info)
                    return text_info
                except:
                    return ""
            else:
                print(response.status_code)
                time.sleep(3)
        except:
            print("章节获取错误重新获取")
            time.sleep(10)


# def main():
#     url = "http://www.biquge.info/0_383/1596644.html"
#     html=get_text(url)
#     print(html)
#     # text = get_text(url)
#     # print(text)
#     # pattern = re.compile('<div id="content"><!--go-->(.*?)<!--over-->', re.S)
#     # text_info = re.findall(pattern, text)
#     # print(text_info)
#
#
# if __name__ == "__main__":
#     main()
