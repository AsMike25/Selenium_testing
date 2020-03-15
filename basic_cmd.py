from selenium import webdriver
import time
# Opening login page by clicking login button on top right of localhost
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("https://lit-scrubland-01256.herokuapp.com/")

time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li/a").click()

time.sleep(5)
driver.quit()