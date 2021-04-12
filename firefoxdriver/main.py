from selenium import webdriver
import time
from fake_useragent import UserAgent

# url = "https://www.w3schools.com/"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()

# change useragennt
options.set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(
    executable_path="/home/tatiana/PycharmProjects/pythonProject1/firefoxdriver/geckodriver",
    options=options)

try:
    driver.get(url="https://ciox.ru/check-user-agent")
    time.sleep(5)
    driver.save_screenshot("vk.png")
    # driver.refresh()
    driver.get_screenshot_as_file("3.png")
    driver.save_screenshot('4.png')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()