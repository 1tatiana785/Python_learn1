from selenium import webdriver
from methods import Authentication
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent= Mozilla/5.0 (X11; Linux x86_64) Chrome/89.0.4389.90")

driver = webdriver.Chrome(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
    options=options)
driver.get(Authentication)
driver.quit()