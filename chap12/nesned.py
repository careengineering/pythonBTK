# def greeting(name):
#     print("Hello ", name)
#
# # print(greeting("Aaaa Bbbb"))
# # print(greeting)
# #
# # Çıktı
# # # Hello  Aaaa Bbbb
# # # None
# # # <function greeting at 0x000001F831DD3E20> - nesne oluşturduğunu gösteriyor
#
# sayHello = greeting
# print(sayHello)
#
# # Çıktı
# # <function greeting at 0x0000025C84223E20>
# # bir öncekinin aynısı / adresi
#
# # print(greeting("Ali"))
# # print(sayHello("Ali"))
# # aynı sonuç
#
#
# del sayHello
# print(sayHello) # hata verir
# print(greeting)
#
# # greeting silmez


#encapsulation
def outer (num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)

outer(10)
# inner_increment(10) # hata verir


def factorial(number):
    if not isinstance(number, int): # gönderilen değerin istenen class olup olmadığına bakar
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero and positive")

    def inner_factorial(number):
        if number <=1:
            return 1

        return number * inner_factorial(number-1)

    return inner_factorial(number)

try:
    print(factorial(6))

except Exception as ex:
    print(ex)