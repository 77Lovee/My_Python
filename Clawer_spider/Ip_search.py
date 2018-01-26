import requests
from bs4 import BeautifulSoup
url="http://m.ip138.com/ip.asp?ip="
ip=input()


try:
  r=requests.get(url+ip)
  r.raise_for_status()
  r.encoding=r.apparent_encoding
  demo=r.text
  soup=BeautifulSoup(demo,'html.parser')
  result=soup.find_all('p','result')
  for res in result:
    print(res.string)

 # print(r.text)
except:
  print("search failed")

~                                                                               
~                            
