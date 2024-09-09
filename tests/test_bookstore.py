import unittest
from src.bookstore import Book, BookStore


class TestBookStore(unittest.TestCase):

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

    def test_list_books(self):
        self.store.list_books()
        store_books = [book.title for book in self.store.books]
        self.assertIn(self.book1.title, store_books)
        self.assertIn(self.book2.title, store_books)

    def test_find_book_by_id(self):
        book = self.store.find_book_by_id(1)
        self.assertEqual(book, self.book1)

    def test_deliver_order(self):
        order = {
            "address": "123 Main St",
            "delivery_time": "Tomorrow 10 AM",
            "payment_method": "Credit Card",
            "books": [self.book1],
        }
        self.store.deliver_order(order)
        self.assertEqual(len(self.store.orders), 1)

    def test_return_book(self):
        self.store.return_book(self.book1)
        self.assertIn(self.book1, self.store.books)


if __name__ == "__main__":
    unittest.main()
