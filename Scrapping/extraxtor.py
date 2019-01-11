import xml.etree.ElementTree as ET
tree = ET.parse('temp_file.xml')
root = tree.getroot()

root = ET.fromstring(country_data_as_string)
# print (root.tag[2])
print ('Attribut: ', root.attrib, type(root.attrib))
print ('Tag: ', root.tag, type(root.tag))
print ('iter: ',root.iter, type(root.iter), '\n\n')

print (root.attrib)
changer = dict(root.attrib)

print (type(changer))

if isinstance(changer, dict):
	for each in changer:
		print ('1:',each)

else:
	print ('Something went completly wrong')


def checkroot():
	count = 0
	for child in root:
		if count <= 3:
			if child.tag == '{http://tempuri.org/sdnList.xsd}':
				pass
			else:
				print (child.tag)
			count +=1
				
#Fucntion for checking types and iterating trhough them
def itteration(*args):
	print (type(args))
	print (len(args))



def findall():
	print ('using ')
	for each in root.findall('Publish_Date'):
		date = str(each.find('Publish_Date').text())
		if date != '':
			print (date)
		else:
			print ('Something went wrong')
