import json

import pytest

from POM.CheckoutandConfimation import Checkout_confirmtion
from POM.Login import LoginPage
from POM.Shop import ShopPage

file_path_data='C:/Users/pc/PycharmProjects/Selenium-Practice/Data/E2Edata.json'
with open(file_path_data) as f:
    test_data = json.load(f)
    test_list=test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_E2Etest(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login=LoginPage(driver)
    login.login(test_list_item["username"],test_list_item["password"])

    Shop_page=ShopPage(driver)
    Shop_page.add_products_to_cart(test_list_item["productName"])
    Shop_page.got_to_Checkout_page()

    Check_and_confirm=Checkout_confirmtion(driver)
    Check_and_confirm.go_to_Checkout_page()
    Check_and_confirm.enter_delivery_address("ind")
    Check_and_confirm.validate_order()


    #
    # # driver.find_element(By.LINK_TEXT, "Shop").click()
    # #
    # # mobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # # for mobile in mobiles:
    # #     name_of_Mobiles = mobile.find_element(By.XPATH, "div/h4/a").text
    # #     if name_of_Mobiles == "Blackberry":
    # #         mobile.find_element(By.XPATH, "div/button").click()
    #
    # # driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
    # driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    # driver.find_element(By.ID, "country").send_keys("ind")
    #
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    # driver.find_element(By.LINK_TEXT, "India").click()
    # driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
    # driver.find_element(By.CSS_SELECTOR, "input[value=Purchase]").click()
    #
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))
    # Sucess_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    # print(Sucess_msg)
    # assert "Success! Thank you!" in Sucess_msg
