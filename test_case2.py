from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
#checking if login is working with correct credentials
driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
driver.get("https://lit-scrubland-01256.herokuapp.com/")
driver.find_element_by_xpath("/html/body/div/div[1]/nav/div/ul/li/a").click()
driver.find_element_by_name("user_name").send_keys("cse17212")
driver.find_element_by_name("password").send_keys("qwertyuiop")
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[1]/div/form/div[3]/div[1]/button").click()
time.sleep(2)
if(driver.current_url != "https://lit-scrubland-01256.herokuapp.com/admin"):
    get_div = driver.find_element_by_css_selector(".text-center > div:nth-child(1) > h2:nth-child(1)").text
    print(get_div)
    if (get_div == "No Such Roll Number Exists"):
        print("Incorrect credentials")
else:
    print("Login Successful")



driver.quit()
