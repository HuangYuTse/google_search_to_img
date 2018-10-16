import requests
import os
from lxml import etree
from urllib.request import urlretrieve
def getimg(url):
	result = requests.get(url) 
	result.encoding = 'utf-8'
	root = etree.fromstring(result.content, etree.HTMLParser())
	txt = root.xpath("//img/@src")
	print(txt)
	x = 0
	for pic in txt:
		urlretrieve(pic,"%s.jpg" %x)
		x += 1
		print("共",x,"張圖片")
if __name__ == '__main__':
	search = input("輸入他媽的字")
	getimg('https://www.google.com.tw/search?tbm=isch&q='+search)

