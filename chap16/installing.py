# pip install selenium
# Selenium driver indir
# https://selenium-python.readthedocs.io/installation.html#instructions-for-windows-users

from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = "http://sadikturan.com"

driver.get(url)