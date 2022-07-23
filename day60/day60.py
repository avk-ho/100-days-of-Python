# https://www.udemy.com/course/100-days-of-code/learn/lecture/22387812#overview

# Day 60
# HTML forms with Flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        return f"<h1>Name: {name}</h1> \
        <h2>Password: {password}</h2>"

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        return f"<h1>Message successfully received.</h1> \
        <ul> \
            <li>Name: {name}</li> \
            <li>Email: {email}</li> \
            <li>Message: {message}</li> \
        </ul>"
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)