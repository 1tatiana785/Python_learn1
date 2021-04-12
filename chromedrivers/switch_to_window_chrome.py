import random
from selenium import webdriver
from const import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import datetime

import time

# options
options = webdriver.ChromeOptions()
# user-agent
options.add_argument("user-agent= Mozilla/5.0 (X11; Linux x86_64) Chrome/89.0.4389.90")

# disable webdriver mode
#options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
#options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
    options=options)

try:
    start_time = datetime.datetime.now()
    driver.get(url=url)
    driver.implicitly_wait(10)
    print("Passing authentication...")
    email_input = driver.find_element_by_id("email")
    email_input.clear()
    email_input.send_keys(login)
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    # login_button = driver.find_element_by_id("buttonFormLogin").click()
    print(driver.window_handles)
    driver.implicitly_wait(10)
    driver.maximize_window()
    companies_menu = driver.find_element_by_xpath(
        "//div[@class = 'app-header__nav-item app-header__select active'][1]//span")
    hover = ActionChains(driver).move_to_element(companies_menu).perform()
    businesses = driver.find_element_by_xpath("//div[@class='app-header__nav-box'][1]//div[@class = 'app-header__select-list'][1]")\
        .click()
    first_company_list = driver.find_element_by_xpath("//ul[@class = 'list-unstyled'][1]")\
        .click()
    company_link = driver.find_element_by_xpath("//td[@class = 'cell-contact table-text'][1]/a/p[2]")\
        .click()
    driver.implicitly_wait(2)
    company_url_link = driver.find_element_by_xpath("//div[@class='company__cell']/a").click()
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    site_info = driver.find_element_by_xpath("//div[@class='hero-big__text']/h1")
    print(f"Info is: {site_info.text}")
    print("-" * 20)
    print(f"Current UPL is: {driver.current_url}")
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    finish_time = datetime.datetime.now() # see now time
    spent_time = finish_time - start_time
    print(spent_time)

except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()