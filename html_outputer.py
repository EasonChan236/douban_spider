#-*- coding: UTF-8 -*-
from io import open
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.txt', 'wb+')
	fout.write('---------------------------\n')
	for data in self.datas:
		for k in data.keys():
			a = k + ":" +data[k]+'\n'
			fout.write(a )
		fout.write('---------------------------\n')
