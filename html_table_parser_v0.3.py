import requests
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata = BeautifulSoup(html_content, "html.parser")
    return soupdata

soup = make_soup("http://directory.psc.gov/hhsdir/eeKey.asp?Key=42857")

r = requests.get(url)

html_content= r.text

soup = BeautifulSoup(html_content, "html.parser")

for tr in soup.find('table')[0]:
	tds=tr.find_all('td')
	print("value 1:%s, value 2:%s\n" % \
		(tds[0].text,tds[1].text))