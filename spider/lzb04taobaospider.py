# -*- coding:utf-8 -*-
import re
import json
import requests
import xlwt

# 信息
data = []

first_url = 'https://s.taobao.com/search?\
initiative_id=tbindexz_20170906&ie=utf8&spm\
=a21bo.50862.201856-taobao-item.2&sourceId\
=tb.index&search_type=item&ssid=s5-e&commend=a\
ll&imgfile=&q=python%E8%A7%86%E9%A2%\
91&suggest=0_2&_input_charset=utf-8\
&wq=python&suggest_query=python&source=suggest'
res = requests.get(first_url)
html = res.text

# 取出所需要的数据
content = re.findall(r'g_page_config = .*g_srp_loadCss', html, re.S)[0]
# 进一步提取，把无效的字符取消掉
content = re.findall(r'{.*}', content)[0]

# 转换成json 格式
content = json.loads(content)

# print(content)
# print(content['mods'])
# print(content['mods']['itemlist'])
# print(content['mods']['itemlist']['data']['auctions'][0])

# 获取信息
data_list = content['mods']['itemlist']['data']['auctions']
for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    data.append(temp)
# print(data[0])
f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)

# 写标题
sheet01.write(0, 0, '标题')
sheet01.write(0, 1, '标价')
sheet01.write(0, 2, '购买人数')
sheet01.write(0, 3, '是否包邮')
sheet01.write(0, 4, '是否天猫')
sheet01.write(0, 5, '地区')
sheet01.write(0, 6, '店名')
sheet01.write(0, 7, 'url')

# 写内容
for i in range(len(data)):
    sheet01.write(i + 1, 0, data[i]['title'])
    sheet01.write(i + 1, 1, data[i]['view_price'])
    sheet01.write(i + 1, 2, data[i]['view_sales'])
    sheet01.write(i + 1, 3, data[i]['view_fee'])
    sheet01.write(i + 1, 4, data[i]['isTmall'])
    sheet01.write(i + 1, 5, data[i]['area'])
    sheet01.write(i + 1, 6, data[i]['name'])
    sheet01.write(i + 1, 7, data[i]['detail_url'])

# 保存
f.save(u'搜索%s的结果.xls' % u'python视频教程')
