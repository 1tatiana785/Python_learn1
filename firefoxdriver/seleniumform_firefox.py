import random
from selenium import webdriver
from const import login, password, url
from selenium.webdriver.common.keys import Keys


import time


# options
options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/firefoxdriver/geckodriver",
    options=options)

try:

    driver.get(url=url)
    time.sleep(3)

    email_input = driver.find_element_by_id("email")
    email_input.clear()
    email_input.send_keys(login)
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    # login_button = driver.find_element_by_id("buttonFormLogin").click()

    time.sleep(3)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()