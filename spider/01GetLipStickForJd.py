#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:EnzoLuo

import re#导入re模块
import urllib.request as eq#导入urllib模块
def pachong(url,page):#建名为pachong的函数，传入两个参数————地址和页码
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
    opener=eq.build_opener()
    opener.addheaders=[headers]
    eq.install_opener(opener)#添加头信息，并安装为全局
    data=eq.urlopen(url).read().decode('utf-8')#抓取网页，并以utf8格式解码
    pat='<img width="220" height="220" class="err-product" data-img="1" source-data-lazy-img="//(img.+?\.jpg)" />'
    imagelist=re.compile(pat).findall(data)#正则表达式匹配图片地址
    x=1#循环标记
    for i in imagelist:
        path='C:/Users/10947/Desktop/lipstick/'+str(page)+str(x)+'.jpg'
        imageurl='http://'+i
        try:#异常处理
            eq.urlretrieve(imageurl,filename=path)
        except eq.URLError as e:
            if hasattr(e,'code'):
                x=x+1
            if hasattr(e,'reason'):
                x=x+1
        x=x+1
for j in range(1,50):#抓取前26页所有口红的图片
    url='https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1&page='+str(j)
    pachong(url,j)