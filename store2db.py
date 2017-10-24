#-*- coding: UTF-8 -*-

from io import open
import re
import sys
import array
import MySQLdb
import time
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect(host="***",user="***",passwd="***",db="***",charset='utf8' )

cursor = db.cursor()

data = []
tag = ['origin:','publisher:','subtitle:','author:','url:','series:','image:','title','binding:','rating:','translator:','tag:','author_ab:','year:','content:','ISBN:','price:','page:']
fh = open ('output.txt')
lines = fh.readlines()

c=''
for b in lines :
	if b == '---------------------------\n' and c:
		data.append(c)
		c = ''
	else:
		c = c+b
for infor in data:
	index = 0
	a =''
	b =''
	store = []
	title = ''
	broke = False
	while index < len(tag):
		
		a = tag[index]
		if index == len(tag) - 1:
			b = ''
		else:
			b = tag[index+1]
		if index == 7:
			try:
				c = re.search(r"subtitle:(.+?)page",str(infor),re.S).group(1)
				title =  re.search(a+"(.+?)"+b,str(c),re.S).group(1).strip('\n').strip(':')
				store.append(MySQLdb.escape_string(title))
			except:
				break	
				broke = True
		else:
			try:
				text =   re.search(a+"(.+)"+b,str(infor),re.S).group(1).strip('\n')
				store.append(MySQLdb.escape_string(text))
			except:
				break
				broke = True
		index = index + 1

	if broke:
		continue
	try:
		sql = "insert into  allbooks (origin,publisher,subtitle,author,url,series,image,title,binding,rating,translator,tag,author_ab,year,content,ISBN,price,page)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (store[0],store[1],store[2],store[3],store[4],store[5],store[6],store[7],store[8],store[9],store[10],store[11],store[12],store[13],store[14],store[15],store[16],store[17])
	except:
		print infor
	try:
	   	# 执行sql语句
	   	cursor.execute(sql)
	   	# 提交到数据库执行
	   	db.commit()
	except Exception,e:
	   	# Rollback in case there is any error
	   	db.rollback()
	   	print title +':insert failed: %s'%str(e) 

# 关闭数据库连接
db.close()
