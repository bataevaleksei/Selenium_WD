from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.execute_script( "return document.getElementById('answer')")
    input1.location_once_scrolled_into_view
    input1.send_keys(y)

    input2=browser.find_element(By.ID,'robotCheckbox')
    input2.location_once_scrolled_into_view
    input2.click()

    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.location_once_scrolled_into_view
    input3.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.location_once_scrolled_into_view
    button.click()

finally:
    time.sleep(5)
    browser.quit()
