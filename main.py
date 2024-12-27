# Принцип єдиної відповідальності (Single Responsibility Principle)

class Order:
    def __init__(self, items):
        self.items = items  

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

class OrderPrinter:
    @staticmethod
    def print_order(order):
        print("\nOrder details:")
        for item in order.items:
            print(f"- {item['name']} (x{item['quantity']}): ${item['price']} each")
        print(f"Total: ${order.calculate_total():.2f}")

class OrderSaver:
    @staticmethod
    def save_order(order):
        print("\nOrder has been saved to the database.")

if __name__ == "__main__":
    items = [
        {'name': 'Laptop', 'price': 1200, 'quantity': 1},
        {'name': 'Mouse', 'price': 25, 'quantity': 2},
        {'name': 'Keyboard', 'price': 75, 'quantity': 1},
    ]

    order = Order(items)

    OrderPrinter.print_order(order)
    OrderSaver.save_order(order)
