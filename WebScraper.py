from bs4 import BeautifulSoup
import re
import requests
import urllib.parse
'''
url = "http://www.livescience.com/36519-diseases-conditions-symptoms-treatments.html"

r  = requests.get(url)

data = r.text
print (data)
soup = BeautifulSoup(data, features="html.parser")
print("here")
for link in soup.find_all('a'):
	print("here")
	print(link.get('href'))
'''

import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
baseurl = "http://www.who.int"
url = "http://www.who.int/news-room/fact-sheets"
response = opener.open(url)
html = response.read()
print(html)
soup = BeautifulSoup(html)
for link in soup.find_all('a'):
	if(re.match( r'/news-room/fact-sheets/detail', link.get('href'), re.M|re.I)):
		print(link.get('href'))
		disease = link.get('href').split('/')[-1]
		print(disease)
		opener = AppURLopener()
		currenturl = baseurl+str(link.get('href'))
		currenturl = urllib.parse.quote(currenturl.encode('utf8'), ':/')
		r = opener.open(currenturl)
		html2 = r.read()
		print(html2)
		soup2 = BeautifulSoup(html2)


		for para in soup2.find_all('div'):
			if(para.get('id')== "PageContent_T0643CD2A003_Col00"):
					print(para)
					text = para.get_text()
					print(text)
					text = text.strip('\n')
					f= open("ScrappedData/"+disease+".txt","w+", encoding="utf-8")
					f.write(text)
					f.close()
		#print(para)