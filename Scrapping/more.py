
def untangle_usage(): 
	import untangle
	obj = untangle.parse('temp_file.xml')

	obj.root.child['name']

def using_lxml():
	import xmltodict
	from time import sleep
	with open('temp_file.xml') as fd:
		doc = xmltodict.parse(fd.read())

	Entries = doc['sdnList']['sdnEntry']
	proc = dict(Entries[0])

	print (type(proc))
	print (proc)
	print (proc['uid'])
	print (proc['lastName'])
	print (proc['sdnType'])
	


def net_fecth():
	# import MySQLdb 
	import pymysql
	import xmltodict
	import requests
	import lxml.html as lh

	url ='https://www.treasury.gov/ofac/downloads/sdn.xml'
	page = requests.get(url)
	doc = lh.fromstring(page.content)

	Entries = page['sdnList']['sdnEntry']
	store = []
	for each in Entries:
		entry = dict(each)
		if isinstance(entry, dict):
			print (entry['uid'], entry['lastName'], entry['sdnType'], '\n')
			store.append(entry)
	
	print (len(store), ' Records stored in the database')

# net_fecth()
test_run()