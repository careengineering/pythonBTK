# def changeName(n):
#  n = "Ada"

#  name = "Yiğit"
#  changeName(name)
#  print(name)


# def change(n):
#  n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# change(sehirler)
# print(sehirler)


# def change(n):
#  n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# change(sehirler[:]) #slicing
# print(sehirler)


def add(a,b,c = 0):
 return sum((a,b))

print(add(10,20))


def add(*params):
 return sum((params))

print(add(10,20,30,50)) 



def displayUser(**args): #dictionary geleceği için iki yıldız
  for key, value in args.items():
   print("{} is {}".format(key,value))

displayUser(name="aaa", age=35, city="istanbul")
displayUser(name="bbb",age=5, city="izmir", phone=123456)
displayUser(name="cccc", age= 20, city="ankara", phone=123456, email="ccc@gmail.com")


def myFunc (a,b, *args, **kwargs):
 print(a)
 print(b)
 print(args)
 print(kwargs)

myFunc(10,20,30,40,50, key1="Value 1", key2="Value 2", )