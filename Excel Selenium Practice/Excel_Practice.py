from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import openpyxl

driver=webdriver.Chrome()
file_path="C://Users//pc//Downloads//download.xlsx"
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"downloadButton").click()

book=openpyxl.load_workbook(file_path)
sheet=book.active
Dict={}
print(sheet.cell(row=3,column=4).value)

for i in range(1,sheet.max_column):
    if sheet.cell(row=1,column=i).value == "Fruit Name":
        print(i)
        break

# for j in range(1,sheet.max_column):
#     if sheet.cell(row=1,column=j).value == "Fruit name":
#         for k in range(1,sheet.max_row):
#             if sheet.cell(row=k,column=j).value == "Apple":
#                 Dict["Row"]=k
#                 break
