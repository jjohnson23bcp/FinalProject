# file created by John Johnson
# base code from Mr. Cozort's soup scraper
# tutorial video: https://www.youtube.com/watch?v=QhD015WUMxE
############## open website with selenium and webdriver ###################
# python library to make HTTP requests, access the internet
import requests
# python package for analyzing HTML and XML documents
from bs4 import BeautifulSoup
# url that will be scraped
URL = 'https://en.wikipedia.org/wiki/List_of_United_States_Military_Academy_alumni'
# get info from website, uses requests library to access the URL
res = requests.get(URL)
# requesting text using BeautifulSoup, html.parser searches the document
soup = BeautifulSoup(res.text, 'html.parser')
# tells code what html to scrape for
titles = soup.find_all("span", attrs={"class":"vcard"})
descriptions = soup.find_all("td", attrs={"class":"note"})
# puts information into a table
table = soup.table
# prints the table
print(table.get_text())