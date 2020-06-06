'''
Created on 06-Jun-2020

@author: gyanesh
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.google.com")
driver.save_screenshot('google.png')
driver.quit()