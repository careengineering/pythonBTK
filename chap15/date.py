# import datetime
from datetime import datetime
from datetime import timedelta
# from datetime import time
# from datetime import date

# yukardakilerden istersen tek tek modülleri lazım olanı ekleyebilirsin.
# ya da direkt import datetime la bütün classları dahil edebilirisn.

simdi = datetime.now()
simdi = datetime.today()

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
print(result)


result = datetime.ctime(simdi)
print(result)

result = datetime.strftime(simdi, "%Y") # yıl
print(result)

result = datetime.strftime(simdi, "%X") # saat
print(result)

result = datetime.strftime(simdi, "%d") # gün
print(result)

result = datetime.strftime(simdi, "%A") # gün - salı
print(result)

result = datetime.strftime(simdi, "%B") # ay tam ad
print(result)


result = datetime.strftime(simdi, "%y %b %a")
print(result)


t = "5 December 2023"
gun, ay, yil = t.split()
print(gun)


t = "1 April 2021 hour 16:50:17"
dt= datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)


birthday = datetime(1985,4,1,16,50,17)
print(birthday)



result = datetime.timestamp(birthday) # tarih objesi saniye cinsinden
print(result)


result = datetime.fromtimestamp(result) # saniyeyi date time çevirir
print(result)


result = datetime.fromtimestamp(0) # 1970 yılından milad alır
result = simdi - birthday # gün - saat bilgisi verir timedelta objesi verir.

result.days
result.seconds
result.microseconds



result = simdi + timedelta(days = 10) # simdiye 10gün ekler
result = simdi - timedelta(days = 10)
print(result)