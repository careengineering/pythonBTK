# Identity Operator - is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) #true
print(x==z) #true

#adres karşılaştırması yapabilmek için

print( x is y) #true
print(x is z) #false
print(x is not z) #true

#Membership Operator - in

x = ["apple", "banana"]
print("apple" in x) #true

name = "xcva"
print("a" in name) #true
print("a" not in name) #false