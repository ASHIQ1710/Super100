class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def reduce_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        else:
            return False


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product, quantity):
        if (product, quantity) in self.items:
            self.items.remove((product, quantity))

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def checkout(self):
        for product, quantity in self.items:
            if not product.reduce_stock(quantity):
                return False
        self.items = []  # Empty the cart after successful checkout
        return True


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_order_to_history(self, order):
        self.order_history.append(order)


class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items
        self.total = total


# Sample products
product1 = Product(1, "Laptop", 1000, 10)
product2 = Product(2, "Headphones", 100, 20)
product3 = Product(3, "Mouse", 20, 50)

# Sample user
user1 = User("user1", "password1")

# Sample shopping cart
cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)

# Sample order
if cart.checkout():
    order = Order(user1, cart.items, cart.calculate_total())
    user1.add_order_to_history(order)
    print("Order placed successfully!")
else:
    print("Insufficient stock to complete the order.")
def print_menu():
    print("===== Main Menu =====")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Cancel order")
    print("6. Exit")
def print_available_products():
    print("Available Products:")
    print("1. Laptop ($1000)")
    print("2. Headphones ($100)")
    print("3. Mouse ($20)")
    print("4. Keyboard ($50)")
    print("5. Smartphone ($500)")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check if the username and password match a user in the system
    # For simplicity, we'll assume there's only one user in this example
    if username == "user1" and password == "password1":
        return User(username, password)
    else:
        print("Invalid username or password.")
        return None


def main():
    # Sample products
    products = [
        Product(1, "Laptop", 1000, 10),
        Product(2, "Headphones", 100, 20),
        Product(3, "Mouse", 20, 50),
        Product(4, "Keyboard", 50, 30),
        Product(5, "Smartphone", 500, 15)
    ]
    user = None

    while user is None:
        print("Please log in to continue.")
        print("Hint: username is user1 and password is password1")
        user = login()

    # Sample shopping cart
    cart = ShoppingCart()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print_available_products()
            product_choice = int(input("Enter product choice: "))
            if 1 <= product_choice <= len(products):
                quantity = int(input("Enter quantity: "))
                cart.add_item(products[product_choice - 1], quantity)
            else:
                print("Invalid product choice.")

        elif choice == '2':
            print("Items in cart:")
            for i, (product, quantity) in enumerate(cart.items, 1):
                print(f"{i}. {product.name} - Quantity: {quantity}")
            item_index = int(input("Enter the item number to remove: ")) - 1
            if 0 <= item_index < len(cart.items):
                item = cart.items[item_index]
                cart.remove_item(item[0], item[1])
            else:
                print("Invalid item number.")

        elif choice == '3':
            print("Items in cart:")
            for i, (product, quantity) in enumerate(cart.items, 1):
                print(f"{i}. {product.name} - Quantity: {quantity}")

        elif choice == '4':
            if cart.items:
                if cart.checkout():
                    order = Order(user1, cart.items, cart.calculate_total())
                    user1.add_order_to_history(order)
                    print("Order placed successfully!")
                else:
                    print("Insufficient stock to complete the order.")
            else:
                print("Cart is empty. Please add items.")

        elif choice == '5':
            cart.items = []
            print("Order canceled. Cart is now empty.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


