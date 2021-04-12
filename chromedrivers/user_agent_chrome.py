import random

from selenium import webdriver
import time
from fake_useragent import UserAgent

# url = "https://news.yahoo.com/"
user_agents_list = [
    "Hell_o",
    "bes_t",
    "pyth_on"
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
options.add_argument("--proxy-server=138.128.91.65:0000")
driver = webdriver.Chrome(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
    options=options)

try:
    # driver.get(url="https://ciox.ru/check-user-agent")

    driver.get(url="https://2ip.ru/")
    time.sleep(5)
    driver.get_screenshot_as_file("1.png")
    driver.save_screenshot('2.png')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()