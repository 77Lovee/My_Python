import requests
import os
url='http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
root='/home/ddd/'
path=root+url.split('/')[-1]
r=requests.get(url)
try:
	with open(path,'wb') as f:
		f.write(r.content)
		f.close()
		print("get sucessfully!")
except:
	print("get failed!")


