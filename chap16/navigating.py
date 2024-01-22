from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #selenium güncelleme
import time


driver = webdriver.Chrome()


url = "http://github.com"
driver.get(url)

# searchInput = driver.find_element(By.ID, 'query-builder-test') #selenium güncelleme

searchInput = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input')

time.sleep(1)

searchInput.send_keys("python")
time.sleep(2)

searchInput.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.page_source
print(result)

# result = driver.find_element(By.CSS_SELECTOR, '.repo-list-item h3 a')

# for element in result:
#    print(element.text)

driver.close()