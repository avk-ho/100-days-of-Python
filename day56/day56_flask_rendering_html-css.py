# https://www.udemy.com/course/100-days-of-code/learn/lecture/22060292#overview

# Day 56
# Rendering HTML CSS files

# Server
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)