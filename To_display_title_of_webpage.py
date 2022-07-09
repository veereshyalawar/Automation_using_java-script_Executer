import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

title = driver.execute_script("return document.title;")
print(title)

#To get alert notifications
driver.execute_script("alert('hello veer');")