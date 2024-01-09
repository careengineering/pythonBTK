import requests
from bs4 import BeautifulSoup

url = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"

# sayfa incele / network / request birini seçip user-agent bak
# User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36

headers = {
    "User-Agent:": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
}


html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"},limit= 20)

print(list)

count = 1

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = li.find("ins").text.strip().strip("TL")
    
    
    print (f"{count}-Name: {name}\nLink: {link}\nOld Price: {oldprice}\nNew Price: {newprice}")
    count+=1


