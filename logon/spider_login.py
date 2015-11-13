#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
from lxml import etree
import re

url = 'http://weibo.cn/qiubomm' #此处请修改为微博地址
url_login = 'https://login.weibo.cn/login/'

html = requests.get(url).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]
print action
print password
print vk
new_url = url_login + action
data = {
    'mobile' : 'ldw5258@163.com',
     password : 'l1625d8521w',
    'remember' : 'on',
    'backURL' : 'http://weibo.cn/qiubomm', #此处请填写微博地址
    'backTitle' : u'微博',
    'tryCount' : '',
    'vk' : vk,
    'submit' : u'登录'
    }
print 'newurl: ',new_url
newhtml = requests.post(new_url,data=data).content
# print 'newhtml', newhtml
new_selector = etree.HTML(newhtml)
# print newhtml.content
page_info = new_selector.xpath('//*[@id="pagelist"]/form/div/text()[2]')
print page_info
page_num = re.findall(r'\d+',page_info[0],re.I)[1]
print "page info: %s" % page_num  # python正则表达式

content = new_selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print text
print 'process page 2'
currunt_page=1
request_url = 'http://weibo.cn/qiubomm'
form_data = {
    'mp' : page_num,
    'page' : '2'
    }
newhtml = requests.post(url,data=form_data).content
print newhtml
new_selector = etree.HTML(newhtml)
content = new_selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print text

#while current_page in range(1,page_num)
#    print 'process page %s ' % current_page
#    form_data['page'] = current_page
#}


