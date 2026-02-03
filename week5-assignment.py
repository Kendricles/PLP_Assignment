"""Assignment: Design Your Own Class + Polymorphism Challenge
- Class examples show constructors, attributes, methods, and encapsulation
- Inheritance layer is demonstrated with `EBook` subclass
- Polymorphism shown using `Vehicle` subclasses implementing `move()` differently
"""


class Book:
    """A simple Book class demonstrating attributes, methods, and encapsulation."""

    def __init__(self, title, author, pages, rating=0.0):
        self.title = title
        self.author = author
        self.pages = pages
        self._rating = float(rating)  # "protected" attribute by convention

    def summary(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def get_rating(self):
        return self._rating

    def set_rating(self, value):
        if not (0.0 <= value <= 5.0):
            raise ValueError("Rating must be between 0.0 and 5.0")
        self._rating = float(value)


class EBook(Book):
    """EBook inherits from Book and adds file-specific info."""

    def __init__(self, title, author, pages, file_size_mb, rating=0.0):
        super().__init__(title, author, pages, rating)
        self.file_size_mb = file_size_mb

    def summary(self):
        return super().summary() + f" (eBook, {self.file_size_mb}MB)"


# Polymorphism challenge: Vehicles with different move() implementations
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


def demo_books():
    print("--- Book & EBook Demo ---")
    book = Book("1984", "George Orwell", 328)
    ebook = EBook("Effective Python", "Brett Slatkin", 256, 3.2)

    print(book.summary())
    print(ebook.summary())

    try:
        ebook.set_rating(4.7)
        print(f"EBook rating set to: {ebook.get_rating()}")
    except ValueError as e:
        print("Failed to set rating:", e)


def demo_polymorphism():
    print("\n--- Vehicle Polymorphism Demo ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()


if __name__ == "__main__":
    demo_books()
    demo_polymorphism()