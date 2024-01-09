import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

# sayfa incele / network / request birini seçip user-agent bak
# User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36

headers = {
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
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


