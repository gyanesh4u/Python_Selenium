'''
Created on 06-Jun-2020

@author: gyanesh
'''
from selenium import webdriver


print("test case started")

#open google chrome browser
driver=webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("python")
#driver.find_element_by_name("btnK").click()
print(driver.title)
driver.quit()
print("test case executed successfully")


