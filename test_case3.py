from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#checking if I can upload a file
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
driver.get("https://lit-scrubland-01256.herokuapp.com/")
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/button").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/button").click()
semester = driver.find_element_by_name("semester")
dropdown = Select(semester)
dropdown.select_by_index(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/form/div[5]/input").send_keys("C:\\Users\\Asus\\Desktop\\samplecsv.csv")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/form/fieldset/div[2]/label/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]").click()
time.sleep(2)
driver.quit()