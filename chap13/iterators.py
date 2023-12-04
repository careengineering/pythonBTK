liste = [1,2,3,4,5]

#------------------------------------------------------------

# for i in liste:
#     print(i)
# # for döngüsü iterarasyon işini yapar / tekrarlama yineleme



#------------------------------------------------------------
# # for yaptığı iş iterator ile yapabiliriz.
# iterator = iter(liste)
# print(iterator)
# # list obje oluşur ...... <list_iterator object at 0x0000015748500310>

# print(next(iterator)) # iteratör üzerindeki elemanlar tek tek ekrana gelir. next her çağrıldığında
# print(next(iterator)) 
# print(next(iterator)) 
# print(next(iterator)) 
# print(next(iterator)) 
# # print(next(iterator)) # 6.eleman olmadığından StopIteration hatası verir



#------------------------------------------------------------
# # farklı bir yöntem

# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break



#------------------------------------------------------------

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start 
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x= self.start
            self.start +=1
            return x
        else:
            raise StopIteration 

list = MyNumbers(10,50)

# # Yöntem 1
# list teki elemanları listeleme
# for x in list:
#     print(x)

# # Yöntem 2
myiter = iter(list)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Yöntem 3 - en sağlıklısı
while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break
