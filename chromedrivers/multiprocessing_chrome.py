from selenium import webdriver
import time
from multiprocessing import Pool
import random


# options
options = webdriver.ChromeOptions()
# user-agent
options.add_argument("user-agent= Mozilla/5.0 (X11; Linux x86_64) Chrome/89.0.4389.90")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True


###########################################################
#   параленьно запускаем в нескольких окнах разные сайты
# urls_list = ["https://preprod.snov.io", "https://test.snov.io", "https://instagram.com"]
#
# def get_date(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
#             options=options)
#         driver.get(url=url)
#         time.sleep(3)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_date, urls_list)


###########################################################
# параленьно запускаем в нескольких окнах один сайт
# urls_list = ["https://preprod.snov.io", "https://test.snov.io", "https://instagram.com"]
#
def get_date(url):
    try:
        driver = webdriver.Chrome(
            executable_path="/home/tatiana/PycharmProjects/pythonProject1/chromedrivers/chromedriver",
            options=options)
        driver.get("https://www.tiktok.com/")
        time.sleep(3)
        driver.find_element_by_class_name("lazyload-wrapper").find_element_by_class_name("item-video-container").click()
        time.sleep(random.randrange(3, 10))
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_date, urls_list)


