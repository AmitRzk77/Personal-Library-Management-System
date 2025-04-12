import json    #ysle file storage and retrive handle garxa, JSON format ma save grna ni help grxa
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename  #file to store
        self.books = []           # list to hold book
        self.load_from_file()   #to read saved book from json file

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not results:
            print("No matching books found.")
        else:
            for book in results:
                print(book)

    def update_book(self, isbn, new_title=None, new_author=None, new_year=None):
        for book in self.books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_year:
                    book.year = new_year
                self.save_to_file()
                print("Book updated successfully.")
                return
        print("Book not found.")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_to_file()
        print("Book deleted successfully.")

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
