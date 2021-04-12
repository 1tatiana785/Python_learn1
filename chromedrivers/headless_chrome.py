import random
from selenium import webdriver
from const import login, password, url
from selenium.webdriver.common.keys import Keys
import pickle
import time

# options
options = webdriver.ChromeOptions()
# user-agent
options.add_argument("user-agent= Mozilla/5.0 (X11; Linux x86_64) Chrome/89.0.4389.90")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
    options=options)

try:

    driver.get(url=url)
    time.sleep(3)
    print("Passing authentication...")
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