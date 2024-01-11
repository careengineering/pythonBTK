import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

# sayfa incele / network / request birini seçip user-agent bak
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

headers = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.n11.com/",
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"   
}


html = requests.get(url, headers=headers).content


print(html)

count = 1

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = li.find("ins").text.strip().strip("TL")
    
    
    print (f"{count}-Name: {name}\nLink: {link}\nOld Price: {oldprice}\nNew Price: {newprice}")
    count+=1


