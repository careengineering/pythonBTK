import os
import datetime


# result = dir(os)
# result = os.name # işletim sistemini söyler


# result = os.getcwd() #etkin dizin öğrenme
# print(result) # D:\....\....\Desktop\Prjct\pythonBTK\chap15


# os.makedir("newdirectory) #klasör oluşturma
# os.makedirs("newdirectory/yeniklasör") #iç içe klasör oluşturma.


# os.chdir("C:\\") #dizin değiştirme
# os.chdir("../../../..") #üst klasörlere geçme


# os.rename("newdirectory","yeniklasör") # klasör adını değiştirme
# os.rmdir("newdirectory") # silmek için
# os.removedirs("yeniklasör/yeniklasör") # alt dizin silmek için

#listeleme
# result = os.listdir() # mevcut klasör içinde listeleme
# result = os.listdir("C:\\") # C içerisinde listeleme


# Sadeve py uzantılı dosyaları listeleme
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)



# dosya bilgilerini verir
# result = os.stat("date.py")

# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişim tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi


# os.system("notepad.exe") # sistm üzerinden istenen uygulama açılır
# print(result)


# #path tam konum verir
# result = os.path.abspath("date.py")

# tam konumu verilen dosyasnın dizin ismini verir
# result = os.path.dirname("D:/..../..../Desktop/Prjct/pythonBTK/chap15/_os.py")

# dosya adı ile dosya yolunu buldurma
# result = os.path.dirname(os.path.abspath("date.py"))

# aranan konumda dosya var mı
# result = os.path.exists("_datetime.py")
# result = os.path.exists("D:/..../..../Desktop/Prjct/pythonBTK/chap15/")

# dosya mı dizin mi sordulama
# result = os.path.isdir("D:/..../..../Desktop/Prjct/pythonBTK/chap15/")
# result = os.path.isfile("D:/..../..../Desktop/Prjct/pythonBTK/chap15/_os.py")

# path bilgilerini birleştirme
# result = os.path.join("C:\\","deneme")

# path bilgilerini bölme
# result = os.path.split("C:\\deneme")

# ulaşılan dosyanın ismi ile uzantısını ayırır
result = os.path.splitext("_os.py")
result = result[0]

print(result)

