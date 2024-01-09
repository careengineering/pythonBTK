# themoviedb.org arşivinden apiyi kullanarak;
# anahtar kelimeye göre arama
# en popüle film listesi
# vizyondaki film listesi

import requests
import json
import os

class theMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/'

        # byme - auth key saklama
        if os.path.exists("mykeys.json"):
            with open("mykeys.json", "r", encoding="utf-8") as file:
                results = json.load(file)
            themoviedb_auth = results["themoviedb_auth"]
             
        self.headers= {
            "accept": "application/json",
            "Authorization": themoviedb_auth
        }

    def searchMovies(self,keyword):
        response = requests.get(self.api_url+'search/keyword?query='+ keyword + '&page=1', headers = self.headers)
        return response.json()    

    def getPopulars(self):      
        response = requests.get(self.api_url+'movie/top_rated?language=en-US&page=1', headers = self.headers)
        return response.json()     
    
    def nowPlaying(self):      
        response = requests.get(self.api_url+'movie/now_playing?language=en-US&page=1', headers = self.headers)
        return response.json()      




movieApi = theMovieDb()


while True:
    secim = input('1- Search with keyword\n2- Most Popular Movie List\n3- Movies now showing\n4- Exit\nChoose: ')

    if secim == '4':
        break

    elif secim == '1':
        keyword = input('Enter keyword(s): ')
        movies = movieApi.searchMovies(keyword)
        for movie in movies['results']:
            print(movie['name'])

    elif secim == '2':
        movies = movieApi.getPopulars()
        for movie in movies['results']:
            print(movie['title'])

    elif secim == '3':
        movies = movieApi.nowPlaying()
        for movie in movies['results']:
            print(movie['title'])   

    else:
        print('yanlış seçim')