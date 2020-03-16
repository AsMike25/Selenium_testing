from selenium import webdriver
import time
#Page refresh
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
driver.get("https://lit-scrubland-01256.herokuapp.com/")
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
time.sleep(2)
a = driver.current_url
driver.refresh()
if(a==driver.current_url):
    print("Page refreshed Successfully")
else:
    print("Page didn't refresh")
time.sleep(2)
driver.quit()