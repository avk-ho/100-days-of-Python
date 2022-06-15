# https://www.udemy.com/course/100-days-of-code/learn/lecture/21377460#overview

# Day 36
# Stock news monitoring project

import requests
import re

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "api_key"
NEWS_API_KEY = "api_key"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Creating the request
stock_url = "https://www.alphavantage.co/query?"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_request = requests.get(url=stock_url, params=stock_params)
stock_request.raise_for_status()
stock_data = stock_request.json()
# print(stock_data)

# Getting the 2 previous stock prices at closing
daily_stock_data = stock_data["Time Series (Daily)"]
last_stock_prices = {}
x = 0
for day in daily_stock_data:
    if x > 1:
        break
    last_stock_prices[day] = daily_stock_data[day]["4. close"]
    # print(day)
    # print(daily_stock_data[day]["4. close"])

    x += 1
# print(last_stock_prices)

# Comparing the 2 last stock prices
def calculatePercentageDifference(last_prices_dict):
    last_prices_list = []
    for date in last_prices_dict:
        last_prices_list.append(float(last_prices_dict[date]))

    prev_day_price = last_prices_list[0]
    prev_day_two_price = last_prices_list[1]

    difference = prev_day_price - prev_day_two_price
    percent_difference = difference / prev_day_price * 100

    return percent_difference

percent_difference = calculatePercentageDifference(last_stock_prices)
# print(percent_difference)

get_news = percent_difference <= -5 or 5 <= percent_difference
# if get_news:
#     print("Get news")
# else:
#     print("Don't get news")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
get_news = True
if get_news:

    # Creating the request
    news_url = "https://newsapi.org/v2/everything?"
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "pageSize": 3,
    }
    news_requests = requests.get(url=news_url, params=news_params)
    news_requests.raise_for_status()
    news_data = news_requests.json()

    # Getting the articles
    news_articles = news_data["articles"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    # Formatting the article
    def formatNewsArticles(news_articles_list):
        message = ""
        for article in news_articles_list:
            headline = article['title']
            description = article["description"]
            message += f"Headline: {headline}\nBrief: {description}\n"
            # regex to clear html tags
            message = re.sub('<[^<]+?>', '', message)
        return message

    news_message = formatNewsArticles(news_articles)

    # Formatting the final sms message
    if percent_difference < 0:
        percent_difference_str = f"🔻{abs(round(percent_difference, 3))}%"
    else:
        percent_difference_str = f"🔺{abs(round(percent_difference, 3))}%"

    sms_message = f'{STOCK}: {percent_difference_str}\n{news_message}'
    print(sms_message)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

