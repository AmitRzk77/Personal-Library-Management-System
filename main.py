from library import Library
from book import Book

def main():
    library = Library()
    while True:
        print("\nPersonal Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, year, isbn))
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            keyword = input("Enter search keyword (title/author): ")
            library.search_books(keyword)
        elif choice == "4":
            isbn = input("Enter ISBN of the book to update: ")
            new_title = input("Enter new title (press enter to skip): ") or None
            new_author = input("Enter new author (press enter to skip): ") or None
            new_year = input("Enter new year (press enter to skip): ") or None
            library.update_book(isbn, new_title, new_author, new_year)
        elif choice == "5":
            isbn = input("Enter ISBN of the book to delete: ")
            library.delete_book(isbn)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
