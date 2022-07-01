# https://www.udemy.com/course/100-days-of-code/learn/lecture/21709134#overview

# Day 47
# Price tracker project

import requests
import smtplib
from bs4 import BeautifulSoup

EMAIL = ""
PASSWORD = ""

# Making the request
product_url = "https://www.amazon.com/Wireless-Bluetooth-Waterproof-Headphones-Android-Black/dp/B085VX9JY7?ref_=Oct_DLandingS_D_0d176598_61&smid=A3531PJZXY3VJY"

# obtained via http://myhttpheader.com/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
}

response = requests.get(url=product_url, headers=headers)

# Getting the html
product_page = response.text
product_soup = BeautifulSoup(product_page, "lxml")

# Getting the product price
product_price = product_soup.select_one("span.apexPriceToPay span.a-offscreen").getText()
product_name = product_soup.select_one("span#productTitle").getText().strip()
# print(product_soup.prettify())
# print(product_price)

def formatPrice(str):
    new_str = str.replace("$", "")
    new_str = new_str.replace("€", "")
    return float(new_str.strip())

product_price = formatPrice(product_price)
# print(product_name)
# print(product_price)
# print(type(product_price))

# Checking the price and sending an email if necessary
TARGET_PRICE = 20.00
if product_price < TARGET_PRICE:
    # print("Below target price.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        
        message = f"The product {product_name} is at {product_price}$ !\n Buy now at {product_url}!"
        # print(message)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)