from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока значение не будет равным 100

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text

    x = calc(x)

    browser.find_element(By.ID, "answer").send_keys(x)

    browser.find_element(By.ID, "solve").click()

    text = browser.switch_to.alert.text
    print(text)

finally:

    time.sleep(5)
    browser.quit()





