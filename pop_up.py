from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("http://localhost:3000/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li/a").click()
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/button").click()
#driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/button").click()