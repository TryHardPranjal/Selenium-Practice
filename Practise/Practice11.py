
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()


Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()
