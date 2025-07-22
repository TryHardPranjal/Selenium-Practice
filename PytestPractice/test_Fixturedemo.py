from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from POM.Login import LoginPage
from POM.Shop import ShopPage


def test_Fixtureconfig(setup):
    print("Good Morning")
    a=2
    b=4
    assert a==b,"Not equal"


def test_E2Etest(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login=LoginPage(driver)
    login.login()

    Shop_page=ShopPage(driver)
    Shop_page.add_products_to_cart("Blackberry")
    Shop_page.got_to_Checkout_page()



    # driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # mobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # for mobile in mobiles:
    #     name_of_Mobiles = mobile.find_element(By.XPATH, "div/h4/a").text
    #     if name_of_Mobiles == "Blackberry":
    #         mobile.find_element(By.XPATH, "div/button").click()

    # driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
    driver.find_element(By.CSS_SELECTOR, "input[value=Purchase]").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))
    Sucess_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    print(Sucess_msg)
    assert "Success! Thank you!" in Sucess_msg
