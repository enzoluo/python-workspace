# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

with open("C:/Users/user/Desktop/python/test/index.html", 'r', encoding='utf-8') as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml', from_encoding='utf-8')

print(soup.original_encoding)

f = open('C:/ZhiBo/workspace/workspacePython/spider/index01.html', 'w', encoding='utf-8')
f.write(str(soup))
f.close()
