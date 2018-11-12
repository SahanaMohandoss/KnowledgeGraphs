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
baseurl = "http://www.myhealthnewsdaily.com/"
url = "https://www.livescience.com/36519-diseases-conditions-symptoms-treatments.html"
response = opener.open(url)
html = response.read()
print(html)
#http://www.myhealthnewsdaily.com/restless-legs-syndrome-symptoms-treatment-0605/

soup = BeautifulSoup(html)
for link in soup.find_all('a'):
	if(re.match( r'http://www.myhealthnewsdaily.com/', link.get('href'), re.M|re.I)):
		print(link.get('href'))
		print(link.string)
		disease = link.string.split(":")[0]
		print(disease)
		
		opener = AppURLopener()
		#currenturl = baseurl+str(link.get('href'))
		currenturl = link.get('href')
		currenturl = urllib.parse.quote(currenturl.encode('utf8'), ':/')
		r = opener.open(currenturl)
		html2 = r.read()
		print(html2)
		
		
		soup2 = BeautifulSoup(html2, features="html.parser")
		
		print("HERE")
		for para in soup2.find_all('div'):
			print(para.get('class'))
			if(para.get('class')):
				if(para.get('class')[0]== "article-content"):
						#print(para)
						print("here")
						text = para.get_text()
						print(text)
						text = text.strip('\n')
						f= open("ScrappedData2/"+disease+".txt","w+", encoding="utf-8")
						f.write(text)
						f.close()
		break
		#print(para)
		