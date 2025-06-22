from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/")
driver.maximize_window()
driver.implicitly_wait(10)

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

print("Enter to quit")
driver.close()