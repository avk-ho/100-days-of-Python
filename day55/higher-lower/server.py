# Guessing game

from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/")
def home():
    return f'<h1>Guess a number between 0 and 9</h1> \
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'

@app.route("/<int:guess>")
def guess(guess):
    if guess == number:
        return f"Congratulations, you found the number ({number}) !!"
    elif guess < number:
        return f"Your guess ({guess}) is too low !"
    elif guess > number:
        return f"Your guess ({guess}) is too high !"

if __name__ == "__main__":
    app.run(debug=True)