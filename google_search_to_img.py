import requests
import os
from lxml import etree
from urllib.request import urlretrieve
from selenium import webdriver
browser = webdriver.Chrome()
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
def img_to_txt(url):
	browser.get(url)
	txt = browser.find_element_by_xpath('//*[@id="topstuff"]/div/div[2]/a')
	print(txt.text)
if __name__ == '__main__':
	search = input("輸入字")
	#getimg('https://www.google.com.tw/search?tbm=isch&q='+search)
	img_to_txt('https://www.google.com/searchbyimage?site=search&sa=X&image_url='+search)

