'''
Created on 06-Jun-2020

@author: gyanesh
'''

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.crmpro.com/")
print(driver.title)
driver.find_element_by_name("username").send_keys("alok4u")
driver.find_element_by_name("password").send_keys("iamalok")
driver.find_element_by_xpath("//input[@value='Login']").click()
print(driver.title)
driver.switch_to_frame(driver.find_element_by_name("mainpanel"))
contacts = driver.find_element_by_xpath("//a[.='Contacts']")
actions = ActionChains(driver)
actions.move_to_element(contacts)
actions.perform()
driver.find_element_by_xpath("//a[.='New Contact']").click()

driver.close()
