import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
best_sellers = driver.find_element(By.PARTIAL_LINK_TEXT,"Best Sellers")
driver.execute_script("arguments[0].click();",best_sellers)
time.sleep(5)
driver.close()