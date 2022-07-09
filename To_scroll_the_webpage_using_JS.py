import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
#to scroll to the bottom of the web page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#to highlight the bottom selected element
highlight = driver.find_element(By.XPATH,"//div[@class = 'navFooterLine navFooterLinkLine navFooterPadItemLine']")
time.sleep(2)
driver.execute_script("arguments[0].style.border = '3px solid red'",highlight)
time.sleep(5)
driver.close()