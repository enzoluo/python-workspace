# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests

url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0"
we_data = requests.get(url)
soup = BeautifulSoup(we_data.text,'lxml')

print(soup.original_encoding)
help(requests.get("https://www.baidu.com").text)
