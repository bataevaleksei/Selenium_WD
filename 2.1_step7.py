from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.TAG_NAME,"img")
    x=x_element.get_attribute("valuex")
    y = calc(x)

    input1=browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    checkbox1=browser.find_element(By.ID,"robotCheckbox")
    checkbox1.click()

    radio1=browser.find_element(By.ID,"robotsRule")
    radio1.click()

    submit1 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submit1.click()
finally:
    time.sleep(5)
    browser.quit()
