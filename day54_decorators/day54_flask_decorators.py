# https://www.udemy.com/course/100-days-of-code/learn/lecture/21928084#overview

# Day 54
# Flask framework // python web dev

# https://flask.palletsprojects.com/en/1.1.x/quickstart/

import time
# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello world"

# if __name__ == "__main__":
#     app.run()


# Exercice
# Create a decorator that mesures execution time of the function it decorates
current_time = time.time()
# print(type(current_time))

def speed_calc_decorator(function):
    def wrapper_function():
        pre_time = time.time()
        function()
        post_time = time.time()
        execution_time = post_time - pre_time
        print(f"Executed in {execution_time}s")

    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()