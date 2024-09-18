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
