from abc import ABC, abstractmethod
from typing import List, Optional

from logger import logger


# SRP: Book class is responsible for book data
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP: Interface for library operations
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


# LSP/OCP: Library class implements the interface
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book '{book.title}' added.")

    def remove_book(self, title: str) -> None:
        book_to_remove: Optional[Book] = None
        for book in self.books:
            if book.title == title:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            logger.info(f"Book '{title}' removed.")
        else:
            logger.info(f"Book '{title}' not found.")

    def show_books(self) -> None:
        if not self.books:
            logger.info("The library is empty.")
        for book in self.books:
            logger.info(book)


# DIP: LibraryManager depends on the abstraction (LibraryInterface)
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library: LibraryInterface = Library()  # Concrete implementation
    manager = LibraryManager(library)  # Depends on abstraction

    while True:
        command: str = (
            input("Enter command (add, remove, show, exit): ").strip().lower()
        )

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting the program.")
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
