from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    # class ^= (начинается с) delivery-root
    element = browser.find_element(By.CSS_SELECTOR, "div[class^=delivery-root]")

    # предок для element:: div[содержит(class='body-root')] child /div[содержит(class='body-title')]
    element = element.find_element(By.XPATH, "ancestor::div[contains(@class,'body-root')]"  # перенос строки
                                             "/div[contains(@class,'body-title')]")

    element.click()
finally:
    time.sleep(5)
    browser.quit()
