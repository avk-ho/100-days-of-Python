# https://www.udemy.com/course/100-days-of-code/learn/lecture/21730018#overview

# Day 45
# Web scraping with beautiful soup

from bs4 import BeautifulSoup
import requests

# Testing with a local html file

# with open("day45/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(type(soup.prettify()))

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)

# Testing with a live website
url = "https://news.ycombinator.com/"

response = requests.get(url=url)
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
all_news = soup.select(".titlelink")
all_scores = soup.select(".score")
# print(len(all_news))
# print(len(all_scores))
news_list = []
for i in range(len(all_news)):
    new_news = {}
    new_news["title"] = all_news[i].getText()
    new_news["url"] = all_news[i].get("href")
    score = int(all_scores[i].getText().split()[0])
    new_news["score"] = score
    news_list.append(new_news)

# print(news_list)
# for news in news_list:
#     print(f"{news['title']} ({news['score']}) - {news['url']}")

def findHighestScoreNews(list):
    highest_score_news = None
    for news in list:
        if highest_score_news is None or highest_score_news["score"] < news["score"]:
            highest_score_news = news

        print(f"{highest_score_news['title']} ({highest_score_news['score']}) - {highest_score_news['url']}")
    return highest_score_news

# findHighestScoreNews(news_list)

# Exercise : create a txt file containing the 100 greatest movies with the url given

greatest_movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=greatest_movies_url)
greatest_movies_website = response.text

movies_soup = BeautifulSoup(greatest_movies_website, "html.parser")
all_movies_titles = movies_soup.find_all(name="h3", class_="title")
# print(len(all_movies_titles))
greatest_movies_txt = ""
for movie in reversed(all_movies_titles):
    greatest_movies_txt += f"{movie.getText()}\n"

with open("day45/greatest_movies.txt", mode="w") as movies_file:
    movies_file.write(greatest_movies_txt)