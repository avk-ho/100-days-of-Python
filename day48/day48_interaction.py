from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Avk\Bureau\Programmes\info\chrome_driver\chromedriver.exe"

# TARGET_URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(TARGET_URL)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# content_portals = driver.find_element(By.PARTIAL_LINK_TEXT, "Content portals")
# # content_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# while True:
#     pass
# driver.quit()

TARGET_URL = "http://secure-retreat-92358.herokuapp.com/"

driver.get(TARGET_URL)
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up_btn = driver.find_element(By.TAG_NAME, "button")

fname.send_keys("First name")
lname.send_keys("Last name")
email.send_keys("mail@mail.com")
sign_up_btn.click()

while True:
    pass