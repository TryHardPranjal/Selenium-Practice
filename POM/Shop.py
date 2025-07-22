from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.Shop_link=(By.LINK_TEXT,"Shop")
        self.products_carts=(By.XPATH, "//div[@class='card h-100']")
        self.checkout_link=(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")


    def add_products_to_cart(self,products_names):
        self.driver.find_element(*self.Shop_link).click()

        mobiles = self.driver.find_elements(*self.products_carts)

        for mobile in mobiles:
            name_of_Mobiles = mobile.find_element(By.XPATH, "div/h4/a").text
            if name_of_Mobiles == "products_names":
                mobile.find_element(By.XPATH, "div/button").click()

    def got_to_Checkout_page(self):
        self.driver.find_element(*self.checkout_link).click()