from selenium import webdriver
import time 
import os
import json



# byme - link saklama
if os.path.exists("mykeys.json"):
    with open("mykeys.json", "r", encoding="utf-8") as file:
        results = json.load(file)
    github_url = results["github_url"]
    github_name = results["github_name"]


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2) # 2 sn bekle
print(driver.title)


driver.maximize_window() # sayfayı tam ekran yapar
driver.save_screenshot("screenshots/github.com-homepage.png") #açılan sayfayı kaydeder




url = github_url
driver.get(url)

print(driver.title)

if github_name in driver.title:
    driver.save_screenshot("screenshots/github-" + github_name + ".png")

time.sleep(2)

driver.back() #sayfayı geri almak
# diver.forward() #sayfayı ileri almak

time.sleep(2)
driver.close()