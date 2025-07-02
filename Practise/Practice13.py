from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
text=driver.find_element(By.CSS_SELECTOR, "ul[class='clearfix'] li").text
assert text=="contact@rahulshettyacademy.com"

Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()