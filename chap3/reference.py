#value type => string, number (float + int)
x = 5
y = 25

x = y
y = 10

# print(x,y)

#reference types => list, class 

a = ["apple", "banana"]
b = ["apple", "banana"]

#listelerde atama beraber hareket eder / adres bilgisi taşıdığı için
a = b
b[0] = "grape"

print(a, b)