from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (\
#     id INTEGER PRIMARY KEY, \
#     title varchar(250) NOT NULL UNIQUE, \
#     author varchar(250) NOT NULL, \
#     rating FLOAT NOT NULL \
#     )"
# )

# Setting up the server with Flask and the database with SQLAlchemy
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

# Create the table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)  

# db.create_all()

# Adding a new book

# hp_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(hp_book)
# db.session.commit()

# all_books = db.session.query(Book).all()

# Forms
class BookForm(FlaskForm):
    book_name = StringField("Book name", validators=[DataRequired()])
    book_author = StringField("Book author", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add book")

class EditRatingForm(FlaskForm):
    new_rating = FloatField("New rating", validators=[DataRequired()])
    submit = SubmitField("Change rating")

# Some CRUD functions
def add_book(title, author, rating):
    new_book = Book(
        title=title,
        author=author,
        rating=rating
    )
    db.session.add(new_book)
    db.session.commit()

def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

##############

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # new_book = {
        #     "title": form.book_name.data,
        #     "author": form.book_author.data,
        #     "rating": form.rating.data
        # }
        # all_books.append(new_book)
        add_book(form.book_name.data, form.book_author.data, form.rating.data)

        return redirect(url_for("home"))

    return render_template("add.html", form=form)

@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    book = Book.query.get(id)
    form = EditRatingForm()

    if form.validate_on_submit():
        book.rating = form.new_rating.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", book=book, form=form)

@app.route("/delete/<id>")
def delete(id):
    delete_book(id)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

