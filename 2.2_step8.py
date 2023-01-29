from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR,"input[name='lastname']")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR,"input[name='email']")
    input3.send_keys("abra@mail.com")

    file1=browser.find_element(By.ID,'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    file1.send_keys(file_path)

    submit1=browser.find_element(By.CLASS_NAME,'btn')
    submit1.click()
finally:
    time.sleep(6)
    browser.quit()