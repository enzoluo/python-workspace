from urllib import request


# 网址
url = "http://www.douban.com/"

# 请求

req = request.Request(url)

# 爬取结果

rep = request.urlopen(req)

data = rep.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
print(data)

# 打印爬取网页的各类信息

print(type(rep))
print(rep.geturl())
print(rep.info())
print(rep.getcode())
