# -*- coding: utf-8 -*-
import re

__author__ = 'chenwei'

import urllib

def getHtml(url):
    # print 'getHtml() url='+url
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'scr="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist


def main():
    pass


if __name__ == '__main__':
    main()

    html = getHtml("http://tieba.baidu.com/p/3741926950")
    # print getImg(html)