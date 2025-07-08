from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
#click on column header
#collect all veggie names->veggielist
#sort this >=newSortedList
#veggieList==newSortedList
browser_Sorted_veggies=[]
driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.CSS_SELECTOR,"th[aria-sort='descending']").click()
veggieWebElements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browser_Sorted_veggies.append(ele.text)

originalSortedVeggies=browser_Sorted_veggies.copy()
browser_Sorted_veggies.sort()
print(originalSortedVeggies)
print(browser_Sorted_veggies)

assert originalSortedVeggies==browser_Sorted_veggies

driver.quit()
