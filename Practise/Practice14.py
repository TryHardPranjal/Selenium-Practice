from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen1.png")

# Answer=input("Enter A to quit: ")
# if Answer=="A":
#     driver.quit()

