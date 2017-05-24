#!/usr/bin/python3
# coding=utf-8
# https://github.com/shengxinjing/my_blog/issues/5
# pyquery是python的一个模块，使用jquery的语法解析html文档
# http://blog.csdn.net/column/details/why-bug.html
import os
import re
import gzip
from urllib import request
from urllib.error import URLError, HTTPError

pwd = os.path.abspath('.')
imgDir = pwd + '/imgs/'

if not os.path.exists(imgDir):
    os.makedirs(imgDir)


def getHtml(url):
    headers = {
        'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': r'gzip, deflate, sdch',
        'Accept-Language': r'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': r'no-cache',
        'Connection': r'keep-alive'
    }

    req = request.Request(
        url,
        data=None,
        headers=headers
    )
    try:
        response = request.urlopen(req)
        print(response.headers.get_content_charset())
        if 'gzip' == response.headers['content-encoding']:
            html = gzip.decompress(response.read()).decode(
                response.headers.get_content_charset())
        else:
            html = response.read().decode(
                response.headers.get_content_charset())
    except HTTPError as e:
        print(e.code())
        # print(e.read())
    return html


'''def getImg(html):
    reg = r'src="(.+?\.(jpg|png))"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist'''


def getImg(pageHtml):
    reg = r'<img.+src="(.+?\.(jpg|png))"'
    imgre = re.compile(reg, re.I)
    imglist = re.findall(imgre, pageHtml)
    x = 0
    # 可优化 enumerate
    for imgurl in imglist:
        name = imgDir + str(x) + '.png'
        request.urlretrieve(imgurl[0], name)
        x += 1

# print(html)
getImg(getHtml("http://www.cnblogs.com/fnng/p/3576154.html"))

# print html
