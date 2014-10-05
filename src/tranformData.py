# -*- coding: utf-8 -*- 


import datetime

import os
import sys


from lxml import html,etree
import StringIO


#處理掉unicode 和 str 在ascii上的問題
reload(sys) 
sys.setdefaultencoding('utf8') 


class PARSER:
	folder= None
	curr  = None
	title = (u"日期",u"日期間距",u"買進匯率",u"賣出匯率",u"差距")
	def __init__(self,folder,curr):
		self.folder = folder
		self.curr = curr
		self.checkFolder()

	def checkFolder(self):
		if os.path.exists(self.folder) == False:
			os.makedirs(self.folder)

	def run(self,t,input_f):
		filepath = "%s/%s.csv"%(self.folder,self.curr)
		f = open(filepath,t)
		source = open(input_f,"r")
		index = 0
		word = ""
		for line in source:
			index = index+1
			line = line.decode("BIG5").encode("UTF-8").replace("<html>","<html><body>").replace("<br>"," ").replace("&nbsp","")
			if index >= 12:
				line  = line.replace("</font></b>","")
			word = word + line
		page=etree.parse(StringIO.StringIO(word)).getroot()
		source.close()
		index = 0
		for row in page.xpath('*//tr'):

			index = index +1
			if index <=1:
				continue

			col = row.xpath(".//td")
			c1 = unicode(col[0].text)
			year = int(c1[0:5])
			month = int(c1[6:8])
			day = int(c1[9:11])
			c2 = col[2].text[1:]
			buy_rate = float(c2)
			c3 = col[3].text[1:]
			sell_rate = float(c3)
			data_dt =  datetime.datetime(year,month,day)
			data_dt_s = data_dt.strftime("%Y%m%d")
			days = (data_dt-datetime.datetime(1970,1,1)).days
			record = (data_dt_s,days,buy_rate,sell_rate,-1.0)
			f.write(",".join(map(str,record))+"\n")
	
		f.close()
	def runRange(self,start,end):
		filepath = "%s/%s.csv"%(self.folder,self.curr)
		try:
			os.remove(filepath)
		except OSError :
			print "No such file"
		f = open(filepath,"w+")
		f.write(",".join(self.title)+"\n")
		f.close()
		for i in xrange(start,end,2):
			start_dt =  str(i)+"0101"
			end_dt = str(i+1)+"1231"
			input_f = "%s/%s_%s_%s.xls"%(self.folder,start_dt,end_dt,self.curr)
			self.run("a+",input_f)


if __name__ =="__main__":	
	p = PARSER(sys.argv[1],sys.argv[2])
	p.runRange(2006,2016)