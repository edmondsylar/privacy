import urllib.request as ur
import requests
import xmltodict
import platform
from os import system as sys
import pymysql
import xmltodict

def fetch():
	url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
	r = requests.get(url, allow_redirects=True)
	cont_type = (r.headers.get('content-type'))

	if cont_type == 'application/xml':
		print ('Progressing........')
		open('temp_file.xml', 'wb').write(r.content)
		print ('Done creating temporary file.')
		
		try:
			fh = open('temp_file.xml')
			sort_and_store()
		except FileNotFoundError:
			print ('File probably could not be fetched')
			return (0)

	else:
		print('The file you are trying to access is not an xml file')

def updater():
	with open('temp_file.xml') as fd:
		check = xmltodict.parse(fd.read())

	Data_published = check['sdnList']['publshInformation']['Publish_Date']
	record_count = check['sdnList']['publshInformation']['Record_Count']
	
	print (str(Data_published))
	print (int(record_count))

	fd.close()

	with open('temp_file.xml') as ch:
		last = xmltodict.parse(ch.read())

	check_update_date = last['sdnList']['publshInformation']['Publish_Date']
	check_rcord_count = last['sdnList']['publshInformation']['Publish_Date']
	print (check_update_date)

	if check_update_date == Data_published:
		print ('No updates found please cheack again letter')
	else:
		print ('Updates available')

updater()

