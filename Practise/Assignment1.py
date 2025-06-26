from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened=driver.window_handles
driver.switch_to.window(windowsOpened[1])
text=driver.find_element(By.CSS_SELECTOR,".im-para.red").text
print(text)
email = re.search(r'[\w.-]+@[\w.-]+', text).group()
print(email)
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.col-md-12").text)


Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()
