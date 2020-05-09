# -*- coding: UTF-8 -*-
# author:enzoluo
from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver

url = "http://www.31xs.net/3/3739/1908354.html"
res = requests.get(url)
res.encoding = "gbk"
soup = BeautifulSoup(res.text,"lxml")

# print(soup)
driver = webdriver.PhantomJS(executable_path='C:/工具/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get(url)
print(driver.page_source)