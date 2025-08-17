from abc import ABC, abstractmethod

# SRP: Book class is responsible for book data
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

# ISP: Interface for library operations
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass

# LSP/OCP: Library class implements the interface
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added.")

    def remove_book(self, title):
        book_to_remove = None
        for book in self.books:
            if book.title == title:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found.")

    def show_books(self):
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book)

# DIP: LibraryManager depends on the abstraction (LibraryInterface)
class LibraryManager:
    def __init__(self, library):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()  # Concrete implementation
    manager = LibraryManager(library) # Depends on abstraction

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print("Exiting the program.")
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
