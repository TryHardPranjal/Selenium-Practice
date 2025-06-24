from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"input#email").clear()
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-email]").send_keys("abc@gmail.com")

input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
driver.quit()