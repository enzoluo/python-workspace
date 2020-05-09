# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re

url = 'https://search.jd.com/Search?keyword=python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B&e' \
      'nc=utf-8&suggest=2.def.0.V08&wq=python&pvid=7343325df11b4f799b88dcb8a1f6fd50'

res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')

# keys = soup.select(' #J_goodsList > ul > li > div > div')
# images = soup.select('#J_goodsList > ul > li > div > div.p-img > a > img')
prices = soup.select('#J_goodsList > ul > li > div > div.p-price > strong')
names = soup.select('#J_goodsList > ul > li > div > div.p-name > a > em')
commits = soup.select('#J_goodsList > ul > li > div > div.p-commit > strong > a')
shopnums = soup.select('#J_goodsList > ul > li > div > div.p-shopnum')

print(shopnums[0])
print(shopnums[1])
print(shopnums[2])
# data
reg_price = re.compile(r'<strong class="J_11461683" data-price="(.*?)"><em>¥</em><i>55.80</i></strong>')
reg_name = re.compile(r'<em><font class="skcolor_ljg">(.*?)</font>')
reg_commit = re.compile(r'<a href="//item.jd.com/\S*.html#comment" id="\S*" \S* target="_blank">(.*?)</a>')
re_shopnum = re.compile(r'<span class="curr-shop"\s*\S*\s*\S*>(.*?)</span>')


def selectData(reg, data, container):
    for x in data:
        temp = re.findall(reg, str(x))
        container.append(temp)

# print(content)
