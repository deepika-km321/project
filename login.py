import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://money.rediff.com/companies")
driver.maximize_window()

# self
# v=driver.find_element(By.XPATH,"//a[contains(text(),'A2Z Infra Engineering Ltd.')]/self::a").text
# print(v)

#parent
# v=driver.find_element(By.XPATH,"//a[contains(text(),'A2Z Infra Engineering Ltd.')]/parent::td").text
# print(v)

#child
# v=driver.find_element(By.XPATH,"//a[contains(text(),'A2Z Infra Engineering Ltd.')]/ancestor::tr/child::td").text
# print(len(v))

#ancestor
v=driver.find_element(By.XPATH,"//a[contains(text(),'A2Z Infra Engineering Ltd.')]/ancestor::tr").text
print(len(v))
