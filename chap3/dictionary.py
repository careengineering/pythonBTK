#key & value

#41 => kocaeli 34=> istanbul

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")]) - sıralı olduğu için aynı index numarasıyla yazabildik.

# plakalar = {"istanbul" : 34, "kocaeli" : 41}
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# print(plakalar)

users = {
"aaaa bbbb" :
 {"age" :35,
 "roles": ["admin", "user"],
  "email": "aaaabbbb@gmail.com",
  "address": "izmir",
  "phone" : 1234567890
 },

 "cccc dddd":
 {"age": 35,
 "roles": ["user"],
 "email": "ccccdddd@gmail.com",
 "address": "istanbul",
 "phone": 9876543210
 }
}


print(users["aaaa bbbb"]["age"])
print(users["aaaa bbbb"]["roles"])