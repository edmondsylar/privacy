import pymysql
import xmltodict

def getter():
	with open('sdn_xml_Sun Dec 16 16-25-51 2018.xml') as fd:
		check = xmltodict.parse(fd.read())

	Date = check['sdnList']['publshInformation']['Publish_Date']

	conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='sanctions')
	cur = conn.cursor()
	cur.execute('SELECT `sdnPublishDate` FROM `t_sdnupdatecheck`')

	if Date in cur:
		print ('exist')
		for r in cur:
			print(r)
	else:
		print ('doesnt Exist.')

getter()
