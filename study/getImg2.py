import urllib.request
import http.cookiejar
import re

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

HEADER = {
    "Host": "www.variflight.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
}


rt = urllib.request.urlopen('http://www.variflight.com/flight/PEK-SYX.html?AE71649A58c77&fdate=20160518')
html = rt.read().decode()
imglist = re.findall('<img src="/flight/detail/([^"]+)"', html)
ut = 'http://www.variflight.com/flight/detail/'
i = 0
for img in imglist:
    i += 1
    url = ut + img
    req = urllib.request.Request(url, None, HEADER)
    rt = urllib.request.urlopen(req)
    fw = open(str(i) + '.png', 'wb')
    fw.write(rt.read())
    fw.close()
    print('save img', i)