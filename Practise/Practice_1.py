
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(50)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR,"button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
# actual_title= driver.title
# expected_title = "OrangeHRM"
# print(driver.current_url)
# if actual_title == expected_title:
#     print("Successfully logged in")
# else:
#     print("Failed to log in")
#
# input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
# driver.quit()

driver.get("https://admin-demo.nopcommerce.com/login")
driver.implicitly_wait(10)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.CLASS_NAME,"login-button").click()
actual_title= driver.title
expected_title = "Dashboard / nopCommerce administration"
print(driver.current_url)
if actual_title == expected_title:
    print("Successfully logged in")
else:
    print("Failed to log in")

input("Press Enter to close the browser...")  # Keeps browser open until you press Enter
driver.quit()

