# -*- coding: utf-8 -*- 

import urllib2
import urllib
import time
from datetime import date

import os
import sys


import re
import tranformData

#處理掉unicode 和 str 在ascii上的問題
reload(sys) 
sys.setdefaultencoding('utf8') 




class CONTROLLER:

	def run(self,parameters):
		if len(parameters)<2:
			raise "# of arguments is too few"
		dl = DOWNLOAD(parameters[1])
		currency = parameters[2]
		for i  in xrange(2006,2016,2):
			start_dt = str(i) + "0101"
			end_dt = str(i+1) + "1231"
			dl.download(start_dt,end_dt,currency)



class DOWNLOAD:
	folder = None
	start_dt = None
	end_dt = None
	def __init__(self,folder):
		self.folder = folder
		self.checkFolder()

	def checkFolder(self):
		if os.path.exists(self.folder) == False:
			os.makedirs(self.folder)

	def download(self,start_dt,end_dt,currency):
		self.start_dt = start_dt
		self.end_dt = end_dt
		server_path = "https://www.cathaybk.com.tw/cathaybk/personal_info14_excel.asp"
		client_path = "%s/%s_%s_%s.xls" % (self.folder,self.start_dt,self.end_dt,currency)
		agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31'
		data = "SelCur=%s3%%AC%%FC%%A4%%B8&R1=2&BDate=%s%%2F%s%%2F%s&EDate=%s%%2F%s%%2F%s" % (currency,self.start_dt[0:4],self.start_dt[4:6],self.start_dt[6:8],self.end_dt[0:4],self.end_dt[4:6],self.end_dt[6:8])
		print server_path
		print client_path
		print data
		cmd = 'curl -A "%s" --data "%s" -o %s %s'% (agent,data,client_path,server_path)
		print cmd
		os.system(cmd)







if __name__ == '__main__':
	CONTROLLER().run(sys.argv)