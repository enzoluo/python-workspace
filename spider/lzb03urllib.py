from urllib import request
from bs4 import BeautifulSoup
url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0"
page = request.urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup.original_encoding)
print(soup)

f = open('C:/ZhiBo/workspace/workspacePython/spider/index.html','w',encoding='utf-8')
text = str(soup)

f.write(text)
f.close()