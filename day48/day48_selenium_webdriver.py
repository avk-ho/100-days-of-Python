# https://www.udemy.com/course/100-days-of-code/learn/lecture/21785294#overview

# Day 48
# Selenium webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Avk\Bureau\Programmes\info\chrome_driver\chromedriver.exe"
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path) #options=chrome_options

# TARGET_URL = "https://www.amazon.com/Wireless-Bluetooth-Waterproof-Headphones-Android-Black/dp/B085VX9JY7?ref_=Oct_DLandingS_D_0d176598_61&smid=A3531PJZXY3VJY"
# driver.get(TARGET_URL)
# price = driver.find_element(By.CSS_SELECTOR, "span.apexPriceToPay")
# print(price.text)

# driver.quit()

TARGET_URL = "https://www.python.org/"
driver.get(TARGET_URL)
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li")
# print(events)
events_list = []
for li in events:
    date = li.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    # print(date)
    event_name = li.find_element(By.TAG_NAME, "a").text
    # print(event_name)
    
    event = {
        "date": date,
        "name": event_name,
    }
    events_list.append(event)

print(events_list)

driver.quit()