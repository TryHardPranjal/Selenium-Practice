import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
driver.find_element(By.CSS_SELECTOR,"button.search-button").click()
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
count=(len(results))
assert count>0
for result in results:
    result.find_element(By.CSS_SELECTOR,"button[type='button']").click()



Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()
