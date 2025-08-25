from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime

# Your original classes
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'
        self.borrow_date = None
        self.return_date = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        return f"Book '{title}' added to the library."

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'available':
                    book.status = 'borrowed'
                    book.borrow_date = datetime.datetime.now()
                    return f"Book '{book.title}' borrowed on {book.borrow_date}."
                else:
                    return f"Book '{book.title}' is already borrowed."
        return "Book not found."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'borrowed':
                    book.status = 'available'
                    book.return_date = datetime.datetime.now()
                    return f"Book '{book.title}' returned on {book.return_date}."
                else:
                    return f"Book '{book.title}' is already available."
        return "Book not found."

    def view_available_books(self):
        return [
            {"title": b.title, "author": b.author, "isbn": b.isbn}
            for b in self.books if b.status == 'available'
        ]

    def view_borrowed_books(self):
        return [
            {
                "title": b.title,
                "author": b.author,
                "isbn": b.isbn,
                "borrow_date": b.borrow_date
            }
            for b in self.books if b.status == 'borrowed'
        ]


# Flask app setup
app = Flask(__name__)
CORS(app)
library = Library()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    data = request.json
    return jsonify({"message": library.add_book(data['title'], data['author'], data['isbn'])})

@app.route("/borrow_book", methods=["POST"])
def borrow_book():
    data = request.json
    return jsonify({"message": library.borrow_book(data['isbn'])})

@app.route("/return_book", methods=["POST"])
def return_book():
    data = request.json
    return jsonify({"message": library.return_book(data['isbn'])})

@app.route("/available_books", methods=["GET"])
def available_books():
    return jsonify(library.view_available_books())

@app.route("/borrowed_books", methods=["GET"])
def borrowed_books():
    return jsonify(library.view_borrowed_books())

if __name__ == "__main__":
    app.run(debug=True)
