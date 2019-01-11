import urllib.request as ur
import json
import requests
import xmltodict
import platform
from time import sleep
from os import system as sys
import os	
os = platform.system()


# Clean up deleting the file s from local machine
def cleanup():
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if '.json' in f:
			print (f)
			print ('Cleaning the working directory')
			if os == 'Windows':
				sys('del /f {}'.format(f))
			else:
				sys('rm -r {}'.format(f))
		else:
			print ('Searching.......')
			sleep(1)
			sys('clear')


# Data Fettcher 
def data_fetch_and_convert():
	print ('using astute API on in {}'.format(os))
	
	if os == 'Windows':
		# sys('del /f temp_file.xml')
		pass

	# return(0)

	url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
	r = requests.get(url, allow_redirects=True)
	cont_type = (r.headers.get('content-type'))
	if cont_type == 'application/xml':
		print ('Progressing........')
		open('temp_file.xml', 'wb').write(r.content)
		print ('Done creating temporary file gettign ready for conversion.')

		# Openning file and creating the json file out of it.
		with open('temp_file.xml', 'r', encoding='utf8') as f:
		
		# Creatign the xmlString
			xmlString = f.read()

		# Creating the jsonString.
		jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

		# creating the json file.
		with open('temp_json.json', 'w', encoding='utf8') as f:
			f.write(jsonString)
			print ('Done creating Json file please check for temp_json.json')
			return (0)
			

	else:
		print('Something went wrong')

data_fetch_and_convert()