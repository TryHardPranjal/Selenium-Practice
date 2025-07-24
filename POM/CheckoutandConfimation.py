from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_confirmtion:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button=(By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.enter_ini_country=(By.ID, "country")
        self.check_named_Country=(By.LINK_TEXT, "India")
        self.select_Checkbox=(By.CSS_SELECTOR, "label[for='checkbox2']")
        self.success_message_locator=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
        self.wait = WebDriverWait(self.driver, 10)
        self.purchase_button=(By.CSS_SELECTOR, "input[value=Purchase]")

    def go_to_Checkout_page(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,country_first3_letters):
        self.driver.find_element(*self.enter_ini_country).send_keys(country_first3_letters)
        #self.driver.find_element(*self.select_Checkbox).click()

        self.wait.until(EC.presence_of_element_located(self.check_named_Country))
        self.driver.find_element(*self.check_named_Country).click()

    def validate_order(self):
        self.driver.find_element(*self.purchase_button).click()
        self.wait.until(EC.presence_of_element_located(self.success_message_locator))
        Success_msg = self.driver.find_element(*self.success_message_locator).text
        print(Success_msg)
        assert "Success! Thank you!" in Success_msg

