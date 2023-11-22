# def sayHello(name = "user"):
#   print("Hello " + name)

# sayHello("aaa")
# sayHello("bbb")
# sayHello()



# def sayHello(name = "user"):
#   return "Hello "+ name 

# msg = sayHello("aaa")
# print(msg)

# def total(num1, num2):
#  return num1 + num2

# result = total (10,20)
# print(result)



def yasHesapla(dogumYili):
  return 2020 - dogumYili

ageAaa = yasHesapla(1985)
ageBbb = yasHesapla(2015)

print(ageAaa, ageBbb)


def EmekliligeKacYilKaldı(dogumYili, isim):

  '''
  DOCSTRING: Doğum yılınıza göre emekliliğe kaç yıl kaldı?
  INPUT: Doğum yılı
  OUTPUT: Hesaplanan doğum yılı
  '''

  yas = yasHesapla(dogumYili)
  emeklilik = 65- yas

  if emeklilik > 0:
    print(f'emekliliğe {emeklilik} yıl kaldı')
  else:
    print('zaten emeklisin')


EmekliligeKacYilKaldı(1983, "Ali")
EmekliligeKacYilKaldı(1950, "Ali")


print(help(EmekliligeKacYilKaldı))