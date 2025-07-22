from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.signin_button=(By.ID,"signInBtn")



    def login(self):
        self.driver.find_element(*self.username).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.signin_button).click()
