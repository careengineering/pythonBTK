import requests 
import json
import os

# byme - auth key saklama
if os.path.exists("mykeys.json"):
    with open("mykeys.json", "r", encoding="utf-8") as file:
        results = json.load(file)
    api_key = results["exchange_api_key"]

api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan Döviz Türü: ") # USD
alinan_doviz = input("Alınan Döviz Türü: ") # TRY

miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, sonuc_json['conversion_rates'][alinan_doviz], alinan_doviz))

print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json['conversion_rates'][alinan_doviz], alinan_doviz))


