# Python Design Patterns and SOLID Principles Tasks

This repository contains two tasks focused on applying design patterns and SOLID principles in Python.

## Task 1: Factory Pattern

### Description

The following code represents a simple system for creating vehicles. We have two classes: `Car` and `Motorcycle`. Each class has a `start_engine()` method that simulates starting the engine of the respective vehicle. Currently, to create a new vehicle, we simply instantiate the corresponding class with the specified make and model.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Motor started")

# Usage
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
```

The next step is to create vehicles with different regional specifications, for example, US Spec and EU Spec.

### Your Task

Implement the Factory pattern to allow creating vehicles with different regional specifications without changing the main vehicle classes.

### Execution Steps

1.  Create an abstract base class `Vehicle` with a `start_engine()` method.
2.  Modify the `Car` and `Motorcycle` classes to inherit from `Vehicle`.
3.  Create an abstract class `VehicleFactory` with `create_car()` and `create_motorcycle()` methods.
4.  Implement two factory classes: `USVehicleFactory` and `EUVehicleFactory`. These factories should create cars and motorcycles with a region-specific tag, for example, `Ford Mustang (US Spec)`.
5.  Modify the initial code to use the factories for creating vehicles.

### Expected Result

Code that allows for easy creation of vehicles for different regions using the corresponding factories.

---

## Task 2: SOLID Principles

### Description

Here is a simplified program for managing a library of books. The program can add new books, remove books, and display all books in the library. The user can interact with the program through the command line using the commands `add`, `remove`, `show`, and `exit`.

```python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f'Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}')

def main():
    library = Library()
    
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        
        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library.remove_book(title)
        elif command == "show":
            library.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```

### Your Task

Rewrite the code to comply with the SOLID principles.

### Execution Steps

1.  **Single Responsibility Principle (SRP):** Create a `Book` class responsible for storing book information.
2.  **Open/Closed Principle (OCP):** Ensure that the `Library` class can be extended with new functionality without modifying its code.
3.  **Liskov Substitution Principle (LSP):** Make sure that any class that inherits from the `LibraryInterface` can replace the `Library` class without breaking the program.
4.  **Interface Segregation Principle (ISP):** Use a `LibraryInterface` to clearly specify the methods required for working with the library.
5.  **Dependency Inversion Principle (DIP):** Make higher-level classes, such as `LibraryManager`, depend on abstractions (interfaces) rather than on concrete implementations of classes.

Follow this structure for your implementation:
```python
from abc import ABC, abstractmethod

class Book:
    pass

class LibraryInterface(ABC):
    pass

class Library(LibraryInterface):
    pass

class LibraryManager:
    pass

def main():
    library = Library()
    manager = LibraryManager(library)

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
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```
