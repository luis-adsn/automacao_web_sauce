from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
sleep(1)

try:
    login_enter = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login_enter.send_keys('standard_user')
    sleep(2)

    password_enter = driver.find_element(By.XPATH,'//input[@id="password"]')
    password_enter.send_keys('secret_sauce')
    password_enter.send_keys(Keys.ENTER)
    sleep(2)

except NoSuchElementException:
    print('Elemento não encontrado')
except Exception as e:
    print('Tente novamente mais tarde')

input()