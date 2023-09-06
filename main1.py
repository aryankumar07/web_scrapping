import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data,"html.parser")


movie = soup.find_all(name="h3",class_="listicleItem_listicle-item__title__hW_Kn")

movie_title = [Movie.getText() for Movie in movie]
movie_list = []
i=1

for name in movie_title:
    pos = 0
    movie_name = ""
    for words in name.split(" "):
        if pos==0:
            pos = pos+1
            movie_name+=f"{i} "
            i+=1
        else:
            movie_name+=words
            movie_name+=" "
    movie_list.append(movie_name)

with open("data.txt",mode="w") as file:
    for name in movie_list:
        file.write(f"{name}\n")
    
   
