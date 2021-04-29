import requests
from bs4 import BeautifulSoup as BS

def getPasteBin (url):
	req = requests.get (url)
	soup = BS (req.content, "html.parser")
	xml = soup.find ("textarea").text
	return xml

def download (url, path):
	open (path, "wb").write (requests.get (url).content)