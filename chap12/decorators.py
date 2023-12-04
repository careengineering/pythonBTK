# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan önceki işlemler")
#         func()
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# # # yöntem 1
# # def sayHello():
# #     print("Hello")
# # sayHello = my_decorator(sayHello)
# # sayHello()


# # yöntem 2
# @my_decorator
# def sayHello():
#     print("Hello")

# sayHello()


#-----------------------------------------------------------------

# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("Aaaa")


#-----------------------------------------------------------------


import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time() # fonksiyonun başlama zamanı
        time.sleep(1) # 1 sn fonksiyonu uyutmak / bekletmek

        func(*args,**kwargs) 

        finish = time.time() # fonksiyonun bitiş zamanı
        print("Fonksiyon " + func.__name__ +" "+ str(finish-start)+ " saniye sürdü") #fonksiyonun adını yazdırdık
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)


usalma(2,3)
faktoriyel(4)
toplama(2,2)
    

