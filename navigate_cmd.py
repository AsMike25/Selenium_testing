from selenium import webdriver
import time

#Navigating between webpages(go to previous page and forward page)

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("https://www.instagram.com/")
print(driver.title)

driver.get("https://web.whatsapp.com/")
print(driver.title)

driver.get("https://www.google.com/")
print(driver.title)

time.sleep(5)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

time.sleep(2)
driver.quit()