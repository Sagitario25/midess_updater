import requests
from bs4 import BeautifulSoup as BS

def getPasteBin (url):
	req = requests.get (url)
	soup = BS (req.content, "html.parser")
	xml = soup.find ("textarea").text
	return xml

def download (url, path):
	content = requests.get (url).content
	file = open (path, "wb")
	file.write (content)
	file.close ()