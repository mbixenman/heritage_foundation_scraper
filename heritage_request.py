import os
from urllib.request import urlopen, Request
import time

if not os.path.exists("heritage_html_files"):
	os.mkdir("heritage_html_files")

for i in range(63):
	url_number = str(i)
	p_number = str(i+1)

	if os.path.exists("heritage_html_files/heritage_page_" + p_number + ".html"):
		print("File for page " + p_number + " already exists")
	else:
		print("Downloading page " + p_number)
		f = open("heritage_html_files/heritage_page_" + p_number + ".html.temp", "wb")
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
		link = 'https://www.heritage.org/voterfraud/search?combine=&state=All&year=&case_type=All&fraud_type=All&fbclid=IwAR3rC0pU32oEwh9NtHcDDGs78bIpV8d3Cd58QT4yag4MoVBKUpTFH37EftA&page=' + url_number
		req = Request(url=link, headers=headers)
		response = urlopen(req)
		html = response.read()
		f.write(html)
		f.close()
		os.rename("heritage_html_files/heritage_page_" + p_number + ".html.temp", "heritage_html_files/heritage_page_" + p_number + ".html")
		time.sleep(180)



