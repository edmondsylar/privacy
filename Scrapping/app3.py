import requests
import lxml.html as lh
import pandas as pd

# url='http://pokemondb.net/pokedex/all'
url ='https://www.treasury.gov/ofac/downloads/sdn.xml'

#handler, page, to  handle teh contents of the website
page = requests.get(url)

#Store the contents pf the website under doc.
doc = lh.fromstring(page.content)

#parse data that is stored between <tr>..</tr> of the HTML
# tr_element = doc.xpath('//table[@class="display"]')
tr_element = doc.xpath('//sdnType')

#check the length of the first 12 rows
print ([len(T) for T in tr_element[:12]])

#Create an Empty list.

col = []
i = 0

for t in tr_element[0]:
	i+=1
	name = t.text_content()
	# print ('%d:"%s"'%(i,name))
	col.append((name, []))

#Since out first row is the header, data is stored on the second row onwards.
for j in range(1, len(tr_element)):
	#T is our j'th row
	T = tr_element[j]

	#if row is not of the size 10, the //tr data is not from our table
	if len(T) != 10:
		break

	#i is the index of our colomn
	i = 0

	#Iterate trhough each element of the row
	for t in T.iterchildren():
		data=t.text_content()
		#Check if row is empty
		if 1>0:
			#convert any numerial value to integers.
			try:
				data=int(data)
			except:
				pass
			#Append the data to the empty list of the i'th colomn
			col[i][1].append(data)
			#Increment i for the net colomn
			i+=1
print ([len(c) for (title, c) in col])

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)

print (df.head())