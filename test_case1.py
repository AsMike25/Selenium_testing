from selenium import webdriver
import time
#Checking if the page titles are displayed
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
driver.get("https://lit-scrubland-01256.herokuapp.com/")
time.sleep(1)
print("Title of "+driver.current_url+" : "+driver.title)
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
print("Title of "+driver.current_url+" : "+driver.title)
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/button").click()
print("Title of "+driver.current_url+" : "+driver.title)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/a/button").click()
print("Title of "+driver.current_url+" : "+driver.title)
driver.back()
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
print("Title of "+driver.current_url+" : "+driver.title)
driver.quit()