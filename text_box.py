from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.maximize_window()

driver.get("http://localhost:3000/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li/a").click()
time.sleep(2)
inp = driver.find_elements_by_class_name("form-control") #give find_element"s" instead of find_element coz u want to check multiple boxes
print(len(inp))
time.sleep(2)
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
time.sleep(2)

driver.quit()
