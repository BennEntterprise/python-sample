import csv


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

    # returns discount price if discount is applied 
    def get_price(self):
        if self.discount:
            return self.discount_price
        
        return self.price

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

    # save inventory to a csv file
    def save_inventory(self):
        with open('inventory.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'price', 'quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()    

            for product_name in self.products:
                writer.writerow({
                    'name': self.products[product_name].name,
                    'price': self.products[product_name].get_price(),
                    'quantity': self.products[product_name].quantity
                })
        
        print("Saved Inventory.")

    # read inventory from a csv file
    def read_inventory(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print('name', 'price', 'quantity')
            for row in reader:
                print(row['name'], row['price'], row['quantity'])


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


# Code to Compare Two Inventory Reports
class InventoryComparer:
    def __init__(self, inventory1, inventory2):
        self.inventory1 = inventory1
        self.inventory2 = inventory2

    def compare_reports(self):
        # Compare product names in both inventories
        common_products = set(self.inventory1.products.keys()) & set(self.inventory2.products.keys())
        unique_products1 = set(self.inventory1.products.keys()) - set(self.inventory2.products.keys())
        unique_products2 = set(self.inventory2.products.keys()) - set(self.inventory1.products.keys())

        # Compare quantities for common products
        quantity_differences = {}
        for product_name in common_products:
            quantity_diff = self.inventory1.products[product_name].quantity - self.inventory2.products[product_name].quantity
            if quantity_diff != 0:
                quantity_differences[product_name] = quantity_diff

        # Generate summary
        summary = f" \
            Common Products : {list(common_products)}, \n \
            Unique Products in Report 1 : {list(unique_products1)}, \n \
            Unique Products in Report 2: {list(unique_products2)}, \n \
            Quantity Differences: {quantity_differences}"

        return summary



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
print()
try:
    inventory.restock_product("Apple", 50)
except ValueError as e:
    print(e)

# listing the products in the inventory
print()
inventory.list_products()

# selling 30 apples
print()
try:
    revenue = inventory.sell_product("Apple", 30)
    print(f"Revenue from sale: ${revenue}")
except ValueError as e:
    print(e)

inventory.list_products()

report = SalesReport(inventory)
report.generate_report()

# applying 10% discount to bananas to the original price
print()
inventory.apply_discount("Banana", 0.1)
inventory.list_products()

# save inventory with discount price
print()
inventory.save_inventory()

# read inventory
print()
inventory.read_inventory('inventory.csv')

# applying 30% discount to bananas to the original price without removing the discount
print()
inventory.apply_discount("Banana", 0.3)
inventory.list_products()

# remove 30% discount from bananas to display the original price
print()
inventory.remove_discount("Banana")
inventory.list_products()

# save inventory with original price
print()
inventory.save_inventory()

# read inventory
print()
inventory.read_inventory('inventory.csv')

# Comparing two database summaries
inventory1 = Inventory()
inventory1.add_product(Product("Apple", 0.50, 100))
inventory1.add_product(Product("Banana", 0.30, 150))

inventory2 = Inventory()
inventory2.add_product(Product("Apple", 0.50, 80))  # Simulating a change in quantity
inventory2.add_product(Product("Orange", 0.40, 120))  # Simulating a new product in the second report

comparer = InventoryComparer(inventory1, inventory2)
summary = comparer.compare_reports()

print()
print("Inventory Comparison Summary:")
print(summary)
