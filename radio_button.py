from selenium import webdriver
import time
#Checking whether radio buttons are selected

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("https://lit-scrubland-01256.herokuapp.com/")

driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li/a").click()
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/button").click()
sel = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/form/fieldset/div[2]/label/input").is_selected()
print("Is it selected :")
print(sel)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/form/fieldset/div[2]/label/input").click()
afsel = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/form/fieldset/div[2]/label/input").is_selected()
print("after clicking ,selected or not :")
print(afsel)
time.sleep(3)
driver.quit()