import urllib2


class HtmlDownloader(object):
    def download(self, url,count):
        if url is None:
            return None
	
	hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
        req = urllib2.Request(url, headers=hds[(count)%len(hds)])
     	response = urllib2.urlopen(req)
	if response.getcode() != 200:
            return None

        return response.read()
