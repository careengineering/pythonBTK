# # global scope

# x = "global scope"

# def function():
#     # local scope
#     x = "local scope"
#     print(x)

# function()
# print(x)



# name = "Aaaa"

# def changeName(new_name):
#     name = new_name
#     print(name)

# changeName("Bbbb")
# print(name)




# name = "global string"

# def greeting():
#     # name= "Aaaa"
#     print("Merhaba "+ name)

#     def hello():
#         # name = "Bbbb"
#         print("Hello "+ name)

#     hello()

# greeting()
# print(name)



x = 50
def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to: {x}")

test()
print(x)