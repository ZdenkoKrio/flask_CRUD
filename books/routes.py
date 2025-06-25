from flask import Blueprint, render_template, request, redirect, url_for
from models import Book
from extensions import db

books_bp = Blueprint("books_bp", __name__, template_folder="templates")


@books_bp.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@books_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("books_bp.index"))
    return render_template("create.html")


@books_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        db.session.commit()
        return redirect(url_for("books_bp.index"))
    return render_template("edit.html", book=book)


@books_bp.route("/delete/<int:id>")
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books_bp.index"))
