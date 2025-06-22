from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get("http://www.rahulshettyacademy.com/client/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("demo@gmail.com")
