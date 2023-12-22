class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.initial_quantity = quantity
        self.quantity = quantity
        self.discount = False
        self.discount_price = None

    def __str__(self):
        return f"{self.name} - ${self.price if not self.discount else self.discount_price} (Quantity: {self.quantity})"

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

    # restocking product
    def restock_product(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name].initial_quantity = self.products[product_name].quantity + quantity
            self.products[product_name].quantity = self.products[product_name].initial_quantity
        else:
            raise ValueError("Product not available or insufficient quantity") 
        
    # applying discount to a product
    def apply_discount(self, product_name, discount):
        if product_name in self.products:
            self.products[product_name].discount = True
            self.products[product_name].discount_price = self.products[product_name].price - (self.products[product_name].price * discount)
        else:
            raise ValueError("Product not available or insufficient quantity")
        
    # removing discount of a product
    def remove_discount(self, product_name):
        if product_name in self.products:
            self.products[product_name].discount = False
        else:
            raise ValueError("Product not available or insufficient quantity")

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

# restocking 50 apples into the inventory
try:
    inventory.restock_product("Apple", 50)
except ValueError as e:
    print(e)

# listing the products in the inventory
inventory.list_products()

# selling 30 apples
try:
    revenue = inventory.sell_product("Apple", 30)
    print(f"Revenue from sale: ${revenue}")
except ValueError as e:
    print(e)

inventory.list_products()

report = SalesReport(inventory)
report.generate_report()

# applying 10% discount to bananas to the original price
inventory.apply_discount("Banana", 0.1)
inventory.list_products()

# applying 30% discount to bananas to the original price without removing the discount
inventory.apply_discount("Banana", 0.3)
inventory.list_products()

# remove 30% discount from bananas to display the original price
inventory.remove_discount("Banana")
inventory.list_products()