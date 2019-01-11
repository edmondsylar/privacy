#import libraries.
import urllib.request as u_lib
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = u_lib.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('div', attrs={'id':'leaderboard'})
# name = name_box.text.strip()

print (name_box)