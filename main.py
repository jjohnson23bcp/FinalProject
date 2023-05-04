# file created by John Johnson
# base code from Mr. Cozort's soup scraper
# tutorial video: https://www.youtube.com/watch?v=QhD015WUMxE
############## open website with selenium and webdriver ###################
# python library to make HTTP requests, access the internet
import requests
# python package for analyzing HTML and XML documents
from bs4 import BeautifulSoup
# url that will be scraped
# https://en.wikipedia.org/wiki/List_of_United_States_Military_Academy_alumni
URL = 'https://bcp.org'
# get info from website, uses requests library to access the URL
res = requests.get(URL)
# shows HTTPError if there is one
res.raise_for_status()
# requesting text using BeautifulSoup, html.parser searches the document
soup = BeautifulSoup(res.text, 'html.parser')
name = soup.findAll("span", attrs={"class":"vcard"})

# print(len(elem))
# turns the html tag into strings
print(str(elem))
# dump into excel



