import numpy as np

# result = np.array([1,3,5,7,9])

# result = np.arange(1,10) # 1..10 arası (10 yok) sayı üretir

# result = np.arange(10,100,3) # 10..100 arası (100 yok) 3 er arttırarak sayı üretir

# result = np.zeros(10) # 10 tane 0 oluşan(float) array
# result = np.ones(10) # 10 tane 1 oluşan(float) array

# result = np.linspace(0,100,5) # başlangıç bitiş eşit aralıklara böler (float sayı tipi)

# result = np.linspace(0,5,5)

# result = np.random.randint(0,10) # 0..10 (10 yok) arasında integer sayı üretir

# result = np.random.randint(20)  # 0..20 (20 yok) arasında integer sayı üretir
# result = np.random.randint(1,10,3) # 0..10 (10 yok) arasında 3 tane integer sayı üretir

# result = np.random.rand(5) # 5 tane sayı üretir
# result = np.random.randn(5) # 5 tane sayı üretir eksi değerler dahil


# np_array = np.arange(50) #0...49 sayı dizisi
# np_multi = np_array.reshape(5,10) # 5 x 10 matris yapar

# print(np_multi.sum(axis=1)) # satırların toplamı
# print(np_multi.sum(axis=0) ) # sütunların toplamı

rnd_numbers = np.random.randint(1,100,10) # 1...99 arasında 10 sayı
print(rnd_numbers)
# result = rnd_numbers.max() # üretilen en büyük sayı
# result = rnd_numbers.min() # üretilen en küçük sayı
# result = rnd_numbers.mean() # üretilen  ortalama sayı
# result = rnd_numbers.argmax() # üretilen en büyük sayının index numarası
result = rnd_numbers.argmin() # üretilen en küçük sayının index numarası
print(result)