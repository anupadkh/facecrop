from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os


def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

image_type = "Action"
# you can change the query for the image  here
query = "sexy+girls"
query= query.split()
query='+'.join(query)
url="https://duckduckgo.com/i.js?l=wt-wt&o=json&q="+query+ "&vqd=103260839796617126753456511166124941715&f=,,,&p=1"

print (url)
header = {'User-Agent': 'Mozilla/5.0'}
soup = get_soup(url,header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
#print images
for img in images:
  raw_img = urllib2.urlopen(img).read()
  print(img)
  #add the directory for your image here
  DIR="testpics/anup/"
  cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
  print (cntr)
  f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
  f.write(raw_img)
  f.close()
