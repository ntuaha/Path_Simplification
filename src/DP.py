# -*- coding: utf-8 -*- 

import urllib2
import urllib
import time
import sys
from datetime import date

class DP:
	data_filepath = None
	output_filepath = None
	threshold = None
	distance_type = None
	last_index = None
	result_array = []
	stack_array = []
	data = []

	def __init__(self,parameters):
		if len(parameters) <4:
			raise "too few paramters to execute"
		[self.data_filepath,self.output_filepath,self.threshold,self.distance_type] = parameters[1:]
		self.threshold = float(self.threshold)

	def distance_1(self,real,predict):
		return abs(real-predict)

	def clear(self):
		del self.result_array[:]
		del self.stack_array[:]
		self.last_index = None

	def readfile(self):
		'''
		讀檔案
		'''
		f = open(self.data_filepath,"r")
		f.readline()
		for line in f:
			record=line.split(",")
			record.append(0)			
			record[1] = int(record[1])
			record[2] = float(record[2])
			record[3] = float(record[3])
			record[4] = float(record[4][:-1])			
			self.data.append(record)
		f.close()

	def simplify(self):
		[start,end] = self.stack_array.pop()
		print end
		print start
		v =  (self.data[end][2]-self.data[start][2])/( self.data[end][1] - self.data[start][1] )
		error_max = 0
		error_ind = -1
		for i in range(start+1,end):
			pred = (self.data[i][1]-self.data[start][1]) * v + self.data[start][2]
			error = self.distance_1(self.data[i][2],pred)
			if error >=error_max:
				error_max = error
				error_ind = i
		if error_ind - start >1:
			self.stack_array.append([start,error_ind])
		if end - error_ind >1:
			self.stack_array.append([error_ind,end])
		#self.result_array.append((end_ind,error_max)
		self.data[error_ind].append(error_max)
		if len(self.stack_array) >0:
			return False
		else:
			return True



	def run(self):
		self.readfile()
		self.last_index = len(self.data)-1
		#self.result_array.append((0,0))
		#self.result_array.append((self.last_index,0))
		self.stack_array.append([0,self.last_index])
		while self.simplify()==False:
			pass
		m = max([self.data[x][6] for x in range(1,self.last_index)])
		self.data[0].append(m)
		self.data[self.last_index].append(m)

		self.output()

	def output(self):
		f = open(self.output_filepath,'w+')
		for record in self.data:
			f.write(",".join(map(str,record))+"\n")
		f.close()


		







if __name__ == '__main__':
	DP(sys.argv).run()