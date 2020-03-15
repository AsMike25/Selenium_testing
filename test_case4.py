from selenium import webdriver
from selenium.webdriver import ActionChains
import time
#Check window minimize,maximize and close functionality
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
driver.get("https://lit-scrubland-01256.herokuapp.com/")
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(2)
driver.close()
