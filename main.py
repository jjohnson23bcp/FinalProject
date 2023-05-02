# file created by John Johnson

############## open website with selenium and webdriver ###################
# python library to make HTTP requests, access the internet
import requests
# python package for analyzing HTML and XML documents
from bs4 import BeautifulSoup

URL = 'https://bcp.org'

# get info from website, uses requests library to access the URL
res = requests.get(URL)
# shows HTTPError if there is one
res.raise_for_status()
# requesting text using BeautifulSoup, html.parser searches the document
soup = BeautifulSoup(res.text, 'html.parser')
# prints the type of object the variable soup is
print(type(soup))
# prints soup
print(soup)
# looking for html tag div
elem = soup.select('div')
# print(len(elem))
# turns the html tag into strings
print(str(elem))
# dump into excel
