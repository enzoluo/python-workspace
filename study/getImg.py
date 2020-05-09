import re
import urllib.request
import urllib
import os


#抓取html 页面
def getHtml(url):
    page = urllib.request.urlopen(url)#非常简单的第三方类库的方法
    html = page.read()

    return html.decode('UTF-8')

#从html里面获取图片
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  # 要加括号，作为元组返回，抓取淘宝的图片png(先看源码中图片的地址路径)reg = r'data-lazy="(.+?\.png)" '
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = 'C:/ZhiBo/assert/images'# 保存在images路径下
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path + '/img'  #设置图片的名字
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{}{}.jpg'.format(paths, x))
        x = x + 1


html = getHtml("http://layerstheme.com/portfolio/html/iCart/")  # 淘宝的：html = getHtml(r"http://www.taobao.com/")
getImg(html)