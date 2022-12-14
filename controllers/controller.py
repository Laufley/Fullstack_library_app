from flask import render_template, Blueprint, redirect
from flask import Blueprint

from models.book import Book
from models.author import Author

from repositories import book_repository, author_repository

books_blueprint = Blueprint("books", __name__)
books_blueprint = Blueprint("authors", __name__)


@books_blueprint.route("/books")
def index():
    books = book_repository.select_all()
    return render_template("index.html", collection = books, writers = authors)


