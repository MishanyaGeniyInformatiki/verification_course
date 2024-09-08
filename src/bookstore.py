class Book:
    def __init__(self, book_id, title, author, year, price, publisher, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.publisher = publisher
        self.genre = genre

    def __str__(self):
        return (f"{self.title} by {self.author} ({self.year}) "
                f"- {self.genre} - ${self.price}")


class BookStore:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to store.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self.books:
                print(book)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def deliver_order(self, order):
        self.orders.append(order)
        print(
            f"Order delivered to {order['address']} at {order['delivery_time']}"
        )

    def return_book(self, book):
        self.books.append(book)
        print(f"Returned {book.title} to store.")
