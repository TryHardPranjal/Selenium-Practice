from selenium.webdriver.common.by import By


class Checkout_confirmtion:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button=(By.CSS_SELECTOR, "button[class='btn btn-success']")







    def go_to_Checkout_page(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self):





    def validate_order(self):


    driver.find_element(By.ID, "country").send_keys("ind")

    driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
    driver.find_element(By.CSS_SELECTOR, "input[value=Purchase]").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))
    Sucess_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    print(Sucess_msg)
    assert "Success! Thank you!" in Sucess_msg