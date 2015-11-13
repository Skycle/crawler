#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
from lxml import etree
import re

cook = {"Cookie": "_T_WM=c4690d282ba9b99a95e54c9e591a71fc; SUB=_2A257QemDDeTxGeRL7FcQ8ynOzjuIHXVYzffLrDV6PUJbrdANLRjZkW17NWf35P3Ur-YbLHOegIzh1x0YdA..; gsid_CTandWM=4utC1d9a1v2DadWdqUZqDaNUt49"}
url = 'http://weibo.cn/qiubomm' #此处请修改为微博网址
# html = requests.get(url).content
# print html
html = requests.get(url, cookies = cook).content
# html = requests.get(url, cookies = cook).text

# html = bytes(bytearray(html, encoding='utf-8'))
#print html

selector = etree.HTML(html)
#page_info = selector.xpath('//*[@id="pagelist"]/form/div/text()[2]')
#page_num = re.findall(r'\d+',page_info[0],re.I)[1]

#print "page info: %s" % page_num  # python正则表达式
weibo_list = selector.xpath('//*[@id="M_D36i5wmyT"]/div')
content = selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    b = 1
    print text

total_page=selector.xpath('//*[@id="pagelist"]/form/div/input[1]/@value')

print 'total page: %s' % (current_page,total_page)

#form_data = {
#    'mp' : page_num,
#    'page' : '2'
#}
#newhtml = requests.post(url,cookies = cook,data=form_data).content
#print newhtml
#new_selector = etree.HTML(newhtml)
#content = new_selector.xpath('//span[@class="ctt"]')
#for each in content:
#    text = each.xpath('string(.)')
#    print text

#while current_page in range(1,page_num)
#    print 'process page %s ' % current_page
#    form_data['page'] = current_page
#}

