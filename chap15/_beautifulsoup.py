# eklenti indirme pip install beautifulsoup4

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
<h1 id="header">
        Python Kursu
    </h1>
    <div class="group1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>

    <div class="group2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>


<div class="group3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <img src="arkaplan.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
  <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify() #html dosyasını düzenler

result = soup.title #html title etiketinin tamamını verir
result = soup.body #html body etiketinin tamamını verir
result = soup.head #html head etiketinin tamamını verir

result = soup.title.name #etiket ismini verir . title
result = soup.title.string #title içindeki bilgiyi verir. İlk Web Sayfam

result = soup.h1 #html h2 etiketinin tamamını verir
result = soup.h1.name #html h2 etiketinin tamamını verir
result = soup.h1.string #h2 içindeki bilgiyi verir.Programlama (ilk h2 verir)

result = soup.h2 #html h2 etiketinin tamamını verir
result = soup.h2.name #html h2 etiketinin tamamını verir
result = soup.h2.string #h2 içindeki bilgiyi verir.Programlama (ilk h2 verir)

result = soup.find_all("h2") #tüm h2 etiketleri liste olarak verir
result = soup.find_all("h2")[0] #tüm h2 etiketlerinde 0.ıncı  verir

result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1]

result = soup.find_all("div")[1].ul
result = soup.find_all("div")[1].ul.li
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren() #alt eleman

result = soup.div.findNextSibling() #aynı düzey elemanlar
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()


# print(result)


result = soup.find_all("a")
for link in result:
    print(link.get("href")) #içerisindeki linkleri alır

