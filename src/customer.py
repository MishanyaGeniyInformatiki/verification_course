class Cart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.books = []

    def add_book_to_cart(self, book):
        self.books.append(book)
        print(f"Added {book.title} to cart.")


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart(cart_id=customer_id)
        self.orders = []

    def add_book_to_cart(self, book):
        self.cart.add_book_to_cart(book)
