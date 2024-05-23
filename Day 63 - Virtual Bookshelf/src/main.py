from flask import Flask, render_template, request, redirect, url_for
from .models import db, Book

# import sqlite3

# db = sqlite3.connect("../data/books-collection.db")
# cursor = db.cursor()

# cursor.execute(
#     """
#     CREATE TABLE books
#     (
#         id INTEGER PRIMARY KEY,
#         title varchar(250) NOT NULL UNIQUE,
#         author varchar(250) NOT NULL,
#         rating FLOAT NOT NULL
#     )
#     """
# )
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Book))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        new_book = Book(
            title=data["book-name"],
            author=data["book-author"],
            rating=data["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        try:
            new_rating = float(request.form["rating"])
            book_to_update.rating = new_rating
            db.session.commit()
        except ValueError:
            pass
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_selected = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    return render_template("edit_rating.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
