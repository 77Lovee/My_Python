#!python3

import requests

def getHtmlText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "Occur to an error!"
if __name__=="__main__":
	url="http://www.github.com"
	print(getHtmlText(url))

