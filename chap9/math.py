#Yöntem 1 (import işlemi için)

# import math

# import math as islem

# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49)
# value = math.ceil(5.6)
# value = math.factorial(6)


# print(value)


# value = islem.factorial(5)



#Yöntem 2

# from math import * - hepsini aldım

# def parametresini math ten önce yazarsan son yükleneni alır
# def sqrt(x):
#     print("x: " + str(x))

from math import factorial, sqrt

# def parametresini math ten sonra yazarsan buna göre hesaplar
# def sqrt(x):
#     print("x: " + str(x))


value = factorial(5)
value = sqrt(144)
print(value)



