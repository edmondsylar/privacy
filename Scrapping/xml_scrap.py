from lxml import etree
def one():
	root = etree.parse('temp_file.xml').getroot()
	instruments = root.find('Instruments')
	instrument = instruments.findall('Instrument')
	for grandchild in instrument:
	    code, source = grandchild.find('Code'), grandchild.find('Source')
	    print (code.text), (source.text)


def sample_code():
	import urllib.request as urllib
	link = "https://www.treasury.gov/ofac/downloads/sdn.xml"
	f = urllib.urlopen(link)
	myfile = f.read()
	print(myfile)

def three():
	from xml.etree import ElementTree as ET
	import requests
	import lxml.html as lh
	from lxml import etree

	# url = 'https://www.treasury.gov/ofac/downloads/sdn.xml'
	# page = requests.get(url)
	# doc = lh.fromstring(page.content)
	imp = etree.parse('temp_file.xml')
	# file = etree.tostring(imp)

	name = ET.fromstring(imp).find('sdnEntry/lastName')

	if name:
		print ('Found name: ', name.text)
	else:
		print('Something went wrong')

three()
