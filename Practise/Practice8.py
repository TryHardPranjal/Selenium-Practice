import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
options=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(options))
for option in options:
    if option.get_attribute("value")=="option2":
        option.click()
        assert option.is_selected()
        break

radio=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radio))
for i in radio:
    if i.get_attribute("value")=="radio2":
        i.click()
        assert i.is_selected()
        break


Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()

