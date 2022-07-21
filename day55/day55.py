# https://www.udemy.com/course/100-days-of-code/learn/lecture/21928088#overview

# Day 55
# Advanced decorators / Rendering html / Parsing urls / Debugging Flask

from flask import Flask

app = Flask(__name__)

# Decorator exercise
def make_bold(function):
    def wrapper_function():
        str = function()
        bold_str = "<b>" + str + "</b>"
        return bold_str

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        str = function()
        underlined_str = "<u>" + str + "</u>"
        return underlined_str

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        str = function()
        emphasis_str = "<em>" + str + "</em>"
        return emphasis_str

    return wrapper_function

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function_name = function.__name__
        returned_value = function(*args)
        
        log = f"You called the function {function_name}{args}.\n \
            It returned {returned_value}."
        print(log)

        function(*args)

    return wrapper

@logging_decorator
def a_func(a, b, c):
    return a + b + c

a_func(1, 2, 3)

# Advanced decorator example
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
    
#     return wrapper


# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s blog post.")


# new_user = User("Test")
# new_user.is_logged_in = True
# create_blog_post(new_user)

# Flask routes

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello world</h1> \
    <p>This is a paragraph.</p> \
    <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"></img>'


@app.route("/<name>")
def greet(name):
    return f"Hello {name}."

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
