import requests
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


def get(url):
    while True:
        resp = requests.get(url, headers=header,timeout=(3, 7))
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            return resp
        else:
            print("请求失败，错误信息：" + resp.text)
            time.sleep(5)
