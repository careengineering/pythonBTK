# generator bellekte yer kaplamayan iterator


#------------------------------------------------------------
# # bu liste bellek üzerinde yer tutar.
# def cube():
#     result = []
#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())



#------------------------------------------------------------
# sadece göstermek için / bellekte yer işgal etmemesi için

def cube():
    for i in range(5):
        yield i**3 # yield ile değer o an üretilir ve kullanılır yer kullanılmaz

for i in cube():
    print(i)



#------------------------------------------------------------
liste = [i**3 for i in range(5)]
print(liste)

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)