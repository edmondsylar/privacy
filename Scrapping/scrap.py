import urllib.request as ur
import requests
import xmltodict
import platform
from os import system as sys
import pymysql
import xmltodict
import time 
import os

num = []
for i in range(35, 903):
	num.append(i)
	
for each in num:
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='tab')
		cur = conn.cursor()
		# sql = "INSERT INTO `kali`(id,dater) VALUES (BIN_TO_UUID(UUID()), 'johnathan')"
		sql = "INSERT INTO t (dater) VALUES ('{}')".format(each)
		
		# cur.execute(delim)
		cur.execute(sql)
		conn.commit()

		print ('worked')
		cur.close()

	except pymysql.Error as err:
		print (err)



"""
DELIMITER //
CREATE TRIGGER init_uuid BEFORE INSERT ON t
  FOR EACH ROW SET NEW.("specified id") = UUID();
//
DELIMITER ;

"""