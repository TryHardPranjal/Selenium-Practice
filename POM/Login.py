from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.signin_button=(By.ID,"signInBtn")



    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_button).click()

    def get_title(self):
        return self.driver.title