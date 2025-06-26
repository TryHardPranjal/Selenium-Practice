import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
driver.find_element(By.CSS_SELECTOR,"button.search-button").click()
time.sleep(2)
Expected_product_name_list=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
list=driver.find_elements(By.CSS_SELECTOR,"div h4")
Actual_list=[]
for i in list:
    Actual_list.append(i.text)
print(Actual_list)
assert Actual_list==Expected_product_name_list

results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
count=(len(results))
assert count>0
for result in results:
    result.find_element(By.CSS_SELECTOR,"button[type='button']").click()
driver.find_element(By.CSS_SELECTOR,"a.cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#sum validation
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)

print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert totalamount==sum

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

Totalafterdiscount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert Totalafterdiscount<totalamount

Answer=input("Enter A to quit: ")
if Answer=="A":
    driver.quit()
