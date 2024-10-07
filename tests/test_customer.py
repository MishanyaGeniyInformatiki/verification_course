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

    def test_remove_book_from_cart(self):
        self.customer.add_book_to_cart(self.book1)
        self.customer.cart.remove_book_from_cart(self.book1.book_id)
        self.assertNotIn(self.book1, self.customer.cart.books)

    def test_view_cart(self):
        self.customer.add_book_to_cart(self.book1)
        self.customer.view_cart()
        cart_books = [book.title for book in self.customer.cart.books]
        self.assertIn(self.book1.title, cart_books)

    def test_checkout(self):
        self.customer.add_book_to_cart(self.book1)
        self.customer.checkout("123 Main St", "Tomorrow 10 AM", "Credit Card")
        self.assertEqual(len(self.customer.orders), 1)
        self.assertEqual(len(self.customer.cart.books), 0)

    def test_return_order(self):
        self.customer.add_book_to_cart(self.book1)
        self.customer.checkout("123 Main St", "Tomorrow 10 AM", "Credit Card")
        self.customer.return_order(0, "Courier", "Defective item")
        self.assertEqual(len(self.customer.orders), 0)

    def test_invalid_return_order(self):
        initial_orders_count = len(self.customer.orders)
        self.customer.return_order(0, "Courier", "Defective item")
        self.assertEqual(len(self.customer.orders), initial_orders_count)

    def test_view_cart_empty(self):
        self.customer.view_cart()


if __name__ == "__main__":
    unittest.main()
