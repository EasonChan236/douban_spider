#-*- coding: UTF-8 -*-

from io import open
import html_downloader
import html_parser
import html_outputer
import urllib2
from bs4 import BeautifulSoup
import re
import urlparse
import time
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderMain(object):
	def __init__(self):
        	self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		self.links = set()

		input1 = open ('./log/log.68','r')
		for line in input1:
			line=line.strip('\n')
			self.links.add(line)
	
	def craw(self):
		count = 0
		while len(self.links)!=0 :
		    	time.sleep(np.random.rand())	
			try:
				new_url = self.links.pop()
				print("craw %d : %s" %(count, new_url))
				html_cont = self.downloader.download(new_url, count)
				new_data = self.parser.paser(new_url, html_cont)
				self.outputer.collect_data(new_data)

			except:
				print('craw failed')
			count= count + 1
		self.outputer.output_html()


if __name__ == '__main__':
	#root_url = "https://baike.baidu.com/item/Python"
	root_url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
	obj_spider = SpiderMain()
	obj_spider.craw()
