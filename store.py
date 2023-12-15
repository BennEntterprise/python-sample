class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} (Quantity: {self.quantity})"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def sell_product(self, product_name, quantity):
        if product_name in self.products and self.products[product_name].quantity >= quantity:
            self.products[product_name].quantity -= quantity
            return self.products[product_name].price * quantity
        else:
            raise ValueError("Product not available or insufficient quantity")

    def list_products(self):
        for product in self.products.values():
            print(product)

class SalesReport:
    def __init__(self, inventory):
        self.inventory = inventory

    def generate_report(self):
        total_sales = 0
        print("Sales Report:")
        for product_name, product in self.inventory.products.items():
            sold_quantity = product.initial_quantity - product.quantity
            if sold_quantity > 0:
                sales = sold_quantity * product.price
                print(f"{product_name}: Sold {sold_quantity}, Total Sales: ${sales}")
                total_sales += sales
        print(f"Total Sales: ${total_sales}")

# Example Usage
inventory = Inventory()
inventory.add_product(Product("Apple", 0.50, 100))
inventory.add_product(Product("Banana", 0.30, 150))

try:
    revenue = inventory.sell_product("Apple", 20)
    print(f"Revenue from sale: ${revenue}")
except ValueError as e:
    print(e)

inventory.list_products()

report = SalesReport(inventory)
report.generate_report()
