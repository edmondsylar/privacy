from lxml import html
import requests

# url = 'http://econpy.pythonanywhere.com/ex/001.html'
url = 'https://scsanctions.un.org/consolidated/'
page = requests.get(url)
tree = html.fromstring(page.content)

# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# prices = tree.xpath('//span[@class="item-price"]/text()')

tables = tree.xpath('//table[@id="sanctions"]/text()')

# print ('Buyers :', buyers)
# print ('Prices :', prices)

# print(type(prices))
# print(type(buyers))

# for buyer in buyers:
# 	for price in prices:
# 		print ('Buyer : {}, Price : {}\n'.format(buyer, price))

# /html/body/div[3]/span

print (type(tables))
print(tables)