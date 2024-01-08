# paket yükleme : pip install requests
# http adresindeki kaynak kodu alır

import requests 
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(result) ----- <Response [200]>
# result = result.text ----- adres üzerinden gelen tüm bilgiyi döker (string olarak)
result = json.loads(result.text)

print(result[0]["title"]) # delectus aut autem yazar

for i in result:
    print(i) # tüm bilgi yazar


for i in result:
    print(i["title"]) # tüm title bilgilerini yazar yazar


for i in result:
    if i["userId"] == 1: # user id 1 olanları listeler
        print(i)
