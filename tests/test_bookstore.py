import unittest
from src.bookstore import Book, BookStore


class TestBookStore(unittest.TestCase):

    def setUp(self):
        self.store = BookStore()

    def test_add_book(self):
        new_book = Book(
            3,
            "Brave New World",
            "Aldous Huxley",
            1932,
            9.99,
            "Chatto & Windus",
            "Dystopian",
        )
        self.store.add_book(new_book)
        self.assertIn(new_book, self.store.books)


if __name__ == "__main__":
    unittest.main()
