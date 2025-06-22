from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By

driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#ID, name, CSS Selector, Class name, tag name, linkText
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.NAME,"email").send_keys("Hello@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Pranjal")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
Answer=input("Enter A to quit: ")

if input=="A":
    driver.quit()





