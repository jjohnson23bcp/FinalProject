# file created by John Johnson


############## open website with selenium and webdriver ###################
import requests
from bs4 import BeautifulSoup

URL = 'https://bcp.org'

# get info from website
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
# print(soup)
elem = soup.select('div')
# print(len(elem))
print(str(elem))
# dump into excel
