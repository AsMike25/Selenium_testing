from selenium import webdriver

#Printing the title and URL of localhost

driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')

driver.get("http://localhost:3000/")

print(driver.title)
print(driver.current_url)
#print(driver.page_source)
driver.close()