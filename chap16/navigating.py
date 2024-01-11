from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #selenium güncelleme
import time


driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME, 'query-builder-test') #selenium güncelleme

# searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)

searchInput.send_keys("python")
time.sleep(2)

searchInput.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.find_element(By.CSS_SELECTOR, '.repo-list-item h3 a')

for element in result:
    print(element.text)

driver.close()