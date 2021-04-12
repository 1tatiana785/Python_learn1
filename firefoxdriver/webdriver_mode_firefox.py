from selenium import webdriver

import time


# options
options = webdriver.FirefoxOptions()
# user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/84.8")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/firefoxdriver/geckodriver",
    options=options)

try:

    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(3)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()