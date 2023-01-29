from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1=browser.find_element(By.ID,'num1')
    num2=browser.find_element(By.ID,'num2')
    sum1=int(num1.text)+int(num2.text)

    select1=Select(browser.find_element(By.TAG_NAME,'select'))
    select1.select_by_visible_text(str(sum1))

    button1=browser.find_element(By.CLASS_NAME,'btn')
    button1.click()
finally:
    time.sleep(5)
    browser.quit()
