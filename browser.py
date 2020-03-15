from selenium import webdriver

#Printing the title and URL of localhost

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("https://lit-scrubland-01256.herokuapp.com/")

print(driver.title)
print(driver.current_url)
#print(driver.page_source)
driver.close()