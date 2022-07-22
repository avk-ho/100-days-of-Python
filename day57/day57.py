# https://www.udemy.com/course/100-days-of-code/learn/lecture/22182706#overview

# Day 57
# Templating with Jinja

import requests
import random
import datetime
from flask import Flask, render_template

BUILDER_NAME = "Alexandre"
CURRENT_YEAR = datetime.datetime.now().year

app = Flask(__name__)


@app.route("/")
def home():
    rand_num = random.randint(0, 9)
    return render_template(
        "index.html", 
        rand_num=rand_num, 
        BUILDER_NAME=BUILDER_NAME, 
        CURRENT_YEAR=CURRENT_YEAR,
        )


@app.route("/guess/<name>")
def guess(name):
    agify_url = f"https://api.agify.io?name={name}"
    genderize_url = f"https://api.genderize.io?name={name}"

    agify_response = requests.get(url=agify_url)
    genderize_response = requests.get(url=genderize_url)

    agify_guess = agify_response.json()["age"]
    genderize_guess = genderize_response.json()["gender"]
    # print(agify_guess)
    # print(genderize_guess)

    return render_template(
        "guess.html",
        BUILDER_NAME=BUILDER_NAME,
        CURRENT_YEAR=CURRENT_YEAR,
        name=name.capitalize(),
        age=agify_guess,
        gender=genderize_guess,
        )


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()

    return render_template(
        "blog.html",
        posts=all_posts
    )


if __name__ == "__main__":
    app.run(debug=True)