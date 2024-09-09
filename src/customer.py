class Cart:
    def __init__(self, cart_id):
        self.cart_id = cart_id
        self.books = []

    def add_book_to_cart(self, book):
        self.books.append(book)
        print(f"Added {book.title} to cart.")

    def remove_book_from_cart(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]
        print(f"Removed book with ID {book_id} from cart.")

    def view_cart(self):
        if not self.books:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for book in self.books:
                print(book)

    def clear_cart(self):
        self.books.clear()
        print("Cart is cleared.")


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart(cart_id=customer_id)
        self.orders = []

    def add_book_to_cart(self, book):
        self.cart.add_book_to_cart(book)

    def view_cart(self):
        self.cart.view_cart()

    def checkout(self, address, delivery_time, payment_method):
        order = {
            "address": address,
            "delivery_time": delivery_time,
            "payment_method": payment_method,
            "books": self.cart.books[:],
        }
        self.orders.append(order)
        print(f"Order checked out for {self.name}:")
        print(f"Address: {address}")
        print(f"Delivery Time: {delivery_time}")
        print(f"Payment Method: {payment_method}")
        self.cart.clear_cart()

    def return_order(self, order_index, return_method, reason):
        if 0 <= order_index < len(self.orders):
            order = self.orders.pop(order_index)
            print(f"Order returned via {return_method} due to '{reason}'.")
            print(f"Books returned: {[book.title for book in order['books']]}")
        else:
            print(f"Invalid order index: {order_index}")
