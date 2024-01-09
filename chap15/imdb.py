import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers = {
           "Accept": "application/json, text/plain, */*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
           "Referer": "https://www.imdb.com/"
           }

html = requests.get(url,headers=headers).content
soup = BeautifulSoup(html, "html.parser")

movies = soup.find("ul", {"class" : "ipc-metadata-list" } ).find_all("li", limit=10)

for movie in movies:
    name = movie.find("h3", {"class": "ipc-title__text"}).text
    ratingStar = movie.find("span", {"class": "ipc-rating-star"}).text
    print(name, ratingStar)



