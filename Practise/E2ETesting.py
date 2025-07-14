from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()

mobiles=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for mobile in mobiles:
    name_of_Mobiles=mobile.find_element(By.XPATH,"div/h4/a").text
    if name_of_Mobiles=="Blackberry":
        mobile.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")

wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[value=Purchase]").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")))
Sucess_msg=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(Sucess_msg)
assert "Success! Thank you!" in Sucess_msg

Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()
