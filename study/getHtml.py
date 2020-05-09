# coding: utf-8
from urllib import request
import os
import re


def firstReptile(url):
    urlData = request.urlopen(url).read()
    # 3.0现在的参数更改了,现在读取的是bytes-like的,但参数要求是chart-like的,如下解码:
    data = urlData.decode("UTF-8")
    objec = re.compile(r'<a href="(http://.+?)" ')
    dir_path = 'C:/ZhiBo/assert'
    path = '\\index'
    image_path = dir_path + path
    if not os.path.isdir(image_path):
        os.makedirs(image_path)
    count = 1
    for item in objec.findall(data):
        image_dir = image_path + '\\' + '{}.html'.format(count)  # 这些地方都用python3，用python2.会出错。
        html = request.urlopen(item).read()
        with open(image_dir, 'wb') as file:
            file.write(html)
        count += 1
        file.close()


if __name__ == '__main__':
    URL = r'https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#replace-with'
    firstReptile(URL)
