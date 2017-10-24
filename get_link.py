
from io import open
import urllib2
from bs4 import BeautifulSoup
import re
import urlparse
import time
import numpy as np
class Get(object):
        def __init__(self):
                self.tag = set()
                self.links = set()

        def iniPar(self, url) :
#		proxies = {'http':'http://10.10.10.10:8765','https':'https://10.10.10.10:8765'}
                header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
                req = urllib2.Request(url, headers=header)
                response = urllib2.urlopen(req)
                cont = response.read()
                soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
                tags = soup.find_all('a', href=re.compile(r'^/tag/'))
		if len(tags) ==0 :
			print 'no tag'
			return
                for a in tags:
                        text = a.get_text()
                        #tail = urllib2.quote(text.encode('utf8'))
                        #newlink = 'https://book.douban.com/tag/' + tail
                        self.tag.add(text)
        def getLinks(self):

                for tag in self.tag:
                        print ( "cate: " + tag+"\n")
                        tail = urllib2.quote(tag.encode('utf8'))
                        link = 'https://book.douban.com/tag/' + tail

                        hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
                        #header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
                        count = 0
                        url = link + '?start='+str(count)+'&type=T' #type can change from T, R and S, with respect to different ranking method for books
                        while (count < 1000 ):
                                #print "page: " + str(count/20 + 1)
				print("page: " +unicode(str(count/20 + 1))+"\n")
                                #print url
                                time.sleep(np.random.rand())
				#time.sleep(random.random())
                                try:
                                        req = urllib2.Request(url, headers=hds[(count/20)%len(hds)])
                                        response = urllib2.urlopen(req)
                                        cont = response.read()
                                        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
                                        links = soup.find_all('a', class_='nbg',href=re.compile(r'^https://book.douban.com/subject/+\d+/$'))
                                        #for a in links:
                                        #       self.links.add(a['href'])
					if len(links) ==0: 
						print 'no book'
						break	
					print "add: "+str(len(links))
                                        for b in links:
                                                self.links.add(b['href'])

                                except:
                                        print ('failed')
                                count = count + 20
                                url = link + '?start='+str(count)+'&type=T'
                                #print len(self.links)
                fout = open('link_set.txt', 'w')

                for link in self.links:
                        fout.write(link + "\n")
if __name__ == '__main__':
        root_url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
        obj_spider = Get()
        obj_spider.iniPar(root_url)
        obj_spider.getLinks()

