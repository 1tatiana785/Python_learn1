from selenium import webdriver
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

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()