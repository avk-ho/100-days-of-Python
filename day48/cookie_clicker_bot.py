from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

chrome_driver_path = "D:\Avk\Bureau\Programmes\info\chrome_driver\chromedriver.exe"

TARGET_URL = "https://orteil.dashnet.org/cookieclicker/"

now = datetime.datetime.now()
loading_time = now + datetime.timedelta(seconds=10)

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(TARGET_URL)

while now < loading_time:
    now = datetime.datetime.now()

lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()

second_loading = now + datetime.timedelta(seconds=10)
while now < second_loading:
    now = datetime.datetime.now()

cookie_btn = driver.find_element(By.ID, "bigCookie")
cookie_per_sec = driver.find_element(By.ID, "cookies")

end_time = now + datetime.timedelta(minutes=1)
five_sec_lapse = now + datetime.timedelta(seconds=5)
test = True

upgrades = driver.find_elements(By.ID, "upgrades")
products = driver.find_elements(By.ID, "products")
cursor_upgrade_one = False
cursor_upgrade_two = False

while now < end_time:
    cookie_btn.click()

    while test:
        print(f"current time : {now}// ending : {end_time}")
        test = False

    if not cursor_upgrade_one:
        products[0].click()
    else:
        pass


    now = datetime.datetime.now()

print(cookie_per_sec.text)
while True:
    pass