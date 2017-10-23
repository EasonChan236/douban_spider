#-*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
	
	links = soup.find('a', class_='nbg')
	res_data['title'] = links['title']
	res_data['image'] = links['href']

	infor = soup.find('div', {'id':'info'})
	auth = ''
	try:
		a= infor.find(text=' 作者').next_element.next_element
		auth = a.string
	except:
		try:
			a= infor.find(text='作者:').next_element.next_element
			auth = a.string
		except:
			pass	
	try:
		while (a.next_sibling) :
			if not a.next_sibling.next_sibling or str(a.next_sibling.next_sibling) == '<br/>' :
				break
			a =a.next_sibling.next_sibling
			auth = auth + '/' + a.string
	except:
		pass
	auth  = auth.strip('/')
	res_data['author'] = ''.join(auth.split())

	if not auth:
		res_data['author'] = '无'
	try:
		res_data['publisher'] = re.search(r"出版社:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['publisher'] = '无'
	try:
		res_data['origin'] = re.search(r"原作名:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['origin'] = '无'
	'''try:
		res_data['translator'] = infor.find_all('a', href=re.compile(r''))[1].get_text().strip()
	except:
		res_data['translator'] = '无'
	'''
	auth = ''
        try:
                a= infor.find(text=' 译者').next_element.next_element
                auth = a.string
        except:
		try:
                	a= infor.find(text='译者:').next_element.next_element
                	auth = a.string
		except:
			pass
	try:
        	while (a.next_sibling) :
                	if not a.next_sibling.next_sibling or str(a.next_sibling.next_sibling) == '<br/>' :
                        	break
                	a =a.next_sibling.next_sibling
                	auth = auth + '/' + a.string
        except:
        	pass
        auth  = auth.strip('/')
        res_data['translator'] = ''.join(auth.split())
	if not auth:
		res_data['translator'] = '无'
        try:
                res_data['publisher'] = re.search(r"出版社:</span>(.+?)<br",str(infor)).group(1).strip()
        except:
                res_data['publisher'] = '无'
        try:
                res_data['origin'] = re.search(r"原作名:</span>(.+?)<br",str(infor)).group(1).strip()
        except:
                res_data['origin'] = '无'

	try:
		res_data['year'] = re.search(r"出版年:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['year'] = '无'
	try:
		res_data['subtitle']= re.search(r"副标题:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['subtitle'] = '无'
	try:
		res_data['page']= re.search(r"页数:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['page'] = '无'
	try:
		res_data['price'] = re.search(r"定价:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['price'] = '无'
	try:
		res_data['binding']= re.search(r"装帧:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['binding'] = '无'
	try:
		res_data['ISBN']= re.search(r"ISBN:</span>(.+?)<br",str(infor)).group(1).strip()
	except:
		res_data['ISBN'] = '无'
	try:
		res_data['series'] = infor.find('a',href=re.compile(r'series')).get_text()
	except:
		res_data['series'] = '无'
	try:
		rate =  soup.find('strong', {'class':'ll rating_num '}).get_text().strip()
		if rate == '':
			res_data['rating'] = '无'
		else:
			res_data['rating'] = rate
	except:
		res_data['rating'] = '无'
	try:
		content = soup.find('div',{"id":"link-report"}).find('span',{'class':'all hidden'}).find('div',{'class':'intro'})
	except:
		try:
			content  = soup.find('div',{'id':'link-report'}).find('div',{'class':'intro'})
		except:
			content = ''
	if content != '':
		content = re.findall(r"<p>(.+?)</p>",str(content))
		b = ''
		for a in content:
			b = b+ '  ' + a + '\n'
		res_data['content'] = b.rstrip()
	else :
		res_data['content'] = '无'
	try:
		content = soup.find('div',{'class':'indent '}).find('span',{"class":"all hidden "}).find('div',{'class':'intro'})
		ab = re.findall(r"<p>(.+?)</p>",str(content))
		b = ''
		for a in ab:
			b = b+ '  ' + a + '\n'
		res_data['author_ab'] = b.rstrip()
	except:
		try:
			content = soup.find('div',{'class':'indent '}).find('div',{'class':'intro'})
	
			ab = re.findall(r"<p>(.+?)</p>",str(content))
			b = ''
			for a in ab:
				b = b+ '  ' + a + '\n'
			res_data['author_ab'] = b.rstrip()

		except:
			res_data['author_ab'] = '无'

	try:
		tags = soup.find('div',{"id":'db-tags-section'}).find_all('a',href=re.compile(r'/tag/')) 
		a = ''
		for tag in tags:
			a = a + '/' + tag.get_text()
		res_data['tag'] = a.strip('/')
	except:
		res_data['tag'] = '无'
	#for k in res_data.keys():
       	#	print k + ": " +res_data[k]

	return res_data

    def paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data
