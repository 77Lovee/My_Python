import requests
from bs4 import BeautifulSoup
def get_movie():
	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36','Host':'movie.douban.com'
}
	movie_list=[]
	for i in range(10):
		link='https://movie.douban.com/top250?start='+str(i*25)
		r=requests.get(link,headers=headers,timeout=10)
		soup=BeautifulSoup(r.text,'lxml')
		div_list=soup.find_all('div','hd')
		for each in div_list:
			movie=each.a.span.text.strip()
			movie_list.append(movie)
	return movie_list

#		print(str(i+1),"webpage responsed code:",r.status_code)
#		print(r.text)
movies=get_movie()
for movie in movies:
  print(movie)
	
