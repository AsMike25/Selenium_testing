from selenium import webdriver
import time
#Implicit wait(If some process takes some,it doesn't wait for it,next line of code is implemented, it waits for the particular process for that particular time)

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("https://lit-scrubland-01256.herokuapp.com/")

time.sleep(3)

driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li/a").click()

driver.implicitly_wait(5)

driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[2]/div/div/a/button").click()

time.sleep(3)

driver.back()