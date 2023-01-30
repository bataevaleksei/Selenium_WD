from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text

    x = calc(x)

    browser.find_element(By.ID,"answer").send_keys(x)

    browser.find_element(By.CLASS_NAME,"btn").click()

    text = browser.switch_to.alert.text
    print(text)

finally:
    time.sleep(5)
    browser.quit()

