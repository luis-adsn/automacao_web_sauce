from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://www.saucedemo.com/')
sleep(1)

try:
    input_login = chrome.find_element(By.XPATH,'//input[@id="user-name"]')
    input_login.send_keys('standard_user')
    sleep(1)

    input_password = chrome.find_element(By.XPATH,'//input[@id="password"]')
    input_password.send_keys('secret_sauce')
    sleep(.5)
    input_password.send_keys(Keys.ENTER)
    sleep(5)

    cart_backpack = chrome.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')
    cart_backpack.click()

    cart_verify = chrome.find_element(By.XPATH,'//div[@id="shopping_cart_container"]')
    cart_verify.click()
    sleep(2)

    checkout_btn = chrome.find_element(By.XPATH,'//button[@id="checkout"]')
    checkout_btn.click()
    sleep(2)

    input_fname = chrome.find_element(By.XPATH,'//input[@id="first-name"]')
    input_fname.send_keys('Luis')
    input_lname = chrome.find_element(By.XPATH,'//input[@id="last-name"]')
    input_lname.send_keys('Neto')
    input_zip = chrome.find_element(By.XPATH,'//input[@id="postal-code"]')
    input_zip.send_keys('13450445')

    continue_btn = chrome.find_element(By.XPATH,'//input[@id="continue"]')
    continue_btn.click()
    sleep(4)

    finish_btn = chrome.find_element(By.XPATH,'//button[@id="finish"]')
    finish_btn.click()
    print('Compra Finalizada!')
    sleep(5)

    back_home_btn = chrome.find_element(By.XPATH,'//button[@id="back-to-products"]')
    back_home_btn.click()

    input()

except NoSuchElementException:
    print('Elemento não encontrado')
except Exception as e:
    print('Tente novamente mais tarde')