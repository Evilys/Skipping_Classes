#!/usr/bin/env python
#coding=gbk
# @Author: Evilys (evilys@foxmail.com)
# @Date:   2016-12-10 01:30:03

import requests
import cookielib
import re

print  '============================================'
print  '               江职旷课查询              		'
print  '            ver 0.1 20161210                '
print  '============================================'
print  '\n'

user = raw_input('学号: ')
password = raw_input('密码: ')

session = requests.session()

session.get('http://jwxt.jmpt.cn:8125/JspHelloWorld/login.jsp')

login_random_payload = {
	'pageId':'000101',
	'actionId':'login',
	'actionmi':'kim'
	}

lgoin_random = session.post('http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet', data=login_random_payload).content

login_random_code = re.findall(r'name="actionmi" value="(.*?)">',lgoin_random)

login_post_01 = session.post('http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet',data={'pageId':'000101','actionId':'login','actionmi':login_random_code[0]})

login_payload = {
	'radiobutton' : 'student', 'pageId' : '000101', 'actionId' : 'login', 'actionmi' : 'm10', 'username' : user, 'password' : password, 'validate' : 'abc', 'osname':'other,?豸:pc'
}
login = session.post('http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet',data=login_payload)

login_content = session.post('http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet',data={'nID':'0','nWeb':'0','pageId':'000201','actionId':'014'})

skip_classes = session.get('http://jwxt.jmpt.cn:8125/JspHelloWorld/BjKqQuery.jsp').content

if '当前在线人数' not in skip_classes:
	print '\n','账号或者密码错误。。。。。'
else:
	skip_classes_code = re.findall(r'<td align="center" class="admincls0">(.*?)</td>\s*<td align="center" class="admincls0">(.*?)</td>\s*<td align="center" class="admincls0">(.*?)</td>\s*<td align="center" class="admincls0">(.*?)</td>\s*<td class="admincls0">',skip_classes)
	print '\n','正常查询旷课节数。。。。。。','\n'	
	if not skip_classes_code:
		print '你没有旷课，棒棒哒！'
	else:
		n = 0
		for q in skip_classes_code:
			for j in q[-1]:
				n += 1
		print '你已经旷了',n,'节课','\n'


raw_input()
