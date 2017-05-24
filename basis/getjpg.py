#!/usr/bin/python
# coding=utf-8
# https://github.com/shengxinjing/my_blog/issues/5
# pyquery是python的一个模块，使用jquery的语法解析html文档
import urllib
import re
import os

pwd = os.path.abspath('.')
imgDir = pwd + '/imgs/'

if not os.path.exists(imgDir):
    os.makedirs(imgDir)


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


'''def getImg(html):
    reg = r'src="(.+?\.(jpg|png))"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist'''


def getImg(html):
    reg = r'src="(.+?\.(jpg|png))"'
    imgre = re.compile(reg, re.I)
    imglist = re.findall(imgre, html)
    x = 0
    # 可优化 enumerate
    for imgurl in imglist:
        urllib.urlretrieve(imgurl[0], imgDir + str(x) + '.png')
        x += 1


html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")
getImg(html)

# print html
