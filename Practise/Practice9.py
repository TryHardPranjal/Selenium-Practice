import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name="Pranjal"
driver=webdriver.Chrome()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"input#alertbtn").click()
alert=driver.switch_to.alert
Alert_text=alert.text
print(Alert_text)
assert name in Alert_text
alert.accept()