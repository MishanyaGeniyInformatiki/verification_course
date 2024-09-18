import unittest
from src.customer import Customer
from src.bookstore import Book, BookStore


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.store = BookStore()
        self.book1 = Book(
            1,
            "To Kill a Mockingbird",
            "Harper Lee",
            1960,
            10.99,
            "J.B. Lippincott & Co.",
            "Fiction",
        )
        self.book2 = Book(
            2,
            "1984",
            "George Orwell",
            1949,
            8.99,
            "Secker & Warburg",
            "Dystopian",
        )
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)
        self.customer = Customer(1, "John Doe")

    def test_add_book_to_cart(self):
        self.customer.add_book_to_cart(self.book1)
        self.assertIn(self.book1, self.customer.cart.books)
        

if __name__ == "__main__":
    unittest.main()
