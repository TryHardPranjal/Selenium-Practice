from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").clear()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("laptop")
driver.find_element(By.XPATH,"//button[@name='submit_search']").click()

input("Press Enter to close the browser...")
driver.quit()