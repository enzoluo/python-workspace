d = {'zhangsan':60,'lisi':70,'wangwu':90,'maliu':30}
print (d)
d['tianqi'] = 100
print(d)
d['maliu'] = 80
print(d)
for x in d:
    print (x +str(d[x]))