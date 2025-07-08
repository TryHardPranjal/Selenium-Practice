from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"downloadButton").click()
file_input=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_path="C://Users//pc//Downloads//download.xlsx"
file_input.send_keys(file_path)

wait=WebDriverWait(driver,5)
toast_locator=(By.CSS_SELECTOR,".Toastify__toast-body")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)

Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()