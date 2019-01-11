import urllib.request as ur
import requests
import xmltodict
import platform
from os import system as sys
import pymysql
import xmltodict
import time 
import os

def check():
	recs = []
	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='sanctions')
	cur = conn.cursor()
	sql="SELECT `sdnUid` FROM `t_sdnentry`"
	cur.execute(sql)
	data = cur.fetchall()
	for each in data:
		for val in each:
			recs.append(val)


	with open('sdn_xml_Mon Dec 17 15-01-22 2018.xml') as file:
		doc = xmltodict.parse(file.read())

	entries = doc['sdnList']['sdnEntry']
	ids = []
	count = 0
	for each in entries:
		entry = dict(each)
		if isinstance(entry, dict):
			uid = entry['uid']
			if uid in recs:
				print ('Exist')
				count +=1
				# pass
			else:
				recs.append(uid)
	print (count)

	# print (len(recs))
	# print (type(recs[12]))
	# # print (recs)


check()