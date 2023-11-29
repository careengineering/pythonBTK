from os import read


# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)

# file.close()


with open("newfile.txt", "r", encoding="utf-8") as file : #bu şekilde close gerek yok. okuma bitince 
    content= file.read()
    print(content)

    print(file.tell()) #cursor yerini söyler

    file.seek(10) #parantez içine pozisyon gönderilir / cursor nereye gitsin
    print(file.tell())
    content2 = file.read()
    print(content2)