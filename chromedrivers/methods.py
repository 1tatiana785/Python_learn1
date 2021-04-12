from selenium import webdriver
from const import login, password, url
from selenium.webdriver.common.keys import Keys

import time

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent= Mozilla/5.0 (X11; Linux x86_64) Chrome/89.0.4389.90")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
    options=options)


class Authentication:
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(1)
    email_input = driver.find_element_by_id("email")
    email_input.clear()
    email_input.send_keys(login)
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password+Keys.ENTER)
    time.sleep(1)

# element_to_hover_over = firefox.find_element_by_id("baz")
#
# hover = ActionChains(firefox).move_to_element(element_to_hover_over)
# hover.perform()

