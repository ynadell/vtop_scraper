from gettext import gettext
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlsxwriter

output= xlsxwriter.Workbook(r'Out.xlsx')
worksheet = output.add_worksheet()
driver = webdriver.Chrome("C:\Selenium Driver\chromedriver.exe")
driver.get("https://vtop.vit.ac.in/vtop/login")
time.sleep(15)
driver.find_element(By.NAME,"username").send_keys("19BDS0094")
driver.find_element(By.NAME,"password").send_keys("PASSWORD")
driver.find_element(By.ID,"submitBtn").click()
time.sleep(90)
i=1
#question  =driver.find_element(By.CLASS_NAME,"sorting_1").text
# question = driver.find_elements(By.XPATH,'//*[@class="sorting_1"]')
#question  =driver.find_elements(By.CLASS_NAME,"sorting_1")
while(i<=2757):
    options = driver.find_elements(By.TAG_NAME,"td")
    # print("Options")
    for x in options:
        worksheet.write(i,0,x.text)
        # print(x.text)
        i+=1
    # page = driver.find_elements(By.TAG_NAME,"a")
    print(i)
    page = driver.find_element(By.XPATH,"//a[text()='Next']").click()
print("all done")
output.close()
# for x in page:
#     print(x.text)
#     if(x.text=="Next"):
        
time.sleep(120)
driver.quit()