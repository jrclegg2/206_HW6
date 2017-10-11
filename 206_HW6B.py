# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

def grabName(url, position):
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   tagWanted = tags[position - 1]
   lastName = tagWanted.contents[0]
   return lastName
def grabLink(url, position):
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   tagWanted = tags[position - 1]
   url = tagWanted.get('href', None)
   return url
url = input("Enter URL: ")
count = int (input ("Enter count: "))
position = int (input("Enter position: "))

i = 0
while (i < count):
   print (grabName(url, position))
   newurl = grabLink(url, position)
   url = newurl
   i += 1
