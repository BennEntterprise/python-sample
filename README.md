# Sample Python

This example is meant to assess basic python code competency. It is not meant to be a trick question, but rather a way to see how you approach a problem and how you think about code.

## Instructions

1. Clone this repository
2. Create a new branch
3. Answer the questions below
4. Commit your changes
5. Push your branch to the remote repository
6. Create a pull request
7. Send an email to let Kyle know you are finished. 

Feel free to use any resources available to you, books, the internet, etc. You may also use any IDE or editor you like.

(Optional) If you would like you can record yourself 'solving the code outloud' while you work through the questions. This is acceptable and also encouraged. If you do chose to record yourself please send the video to Kyle as well as either a link to the video or the video file itself. Since this repository is open source you are more than welcome to use that vied as part of your portfolio and feel free to share it with others during your career search.

## Questions:

These can be answered right here in the README.md file. You can also create a new file and answer them there if you prefer.

### Written questions 

1) How does the Inventory class track and update the quantity of products?
   
The Inventory class tracks and updates the quantity of products through the ‘products’ attribute, which is a dictionary where the keys are product names, and the values are instances of the `Product` class.

Let's break down the relevant methods:

i. Adding Products:
   
When a new product is added to the inventory using the ‘add_product’ method, the method checks whether the product with the same name already exists in the ‘products’ dictionary. If it does, the method updates the quantity of the existing product by adding the new quantity. If it doesn't exist, a new entry is added to the ‘products’ dictionary.

    
    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product
    

ii. Selling Products:
   When a product is sold using the ‘sell_product’ method, it decreases the quantity of the corresponding product in the ‘products’ dictionary. It checks if the product exists and if the quantity to be sold is available before updating the quantity.

  
    def sell_product(self, product_name, quantity):
        if product_name in self.products and self.products[product_name].quantity >= quantity:
            self.products[product_name].quantity -= quantity
            return self.products[product_name].price * quantity
        else:
            raise ValueError("Product not available or insufficient quantity")

<br>

2) In the SalesReport class, how is the total sales figure calculated?
   
The total sales figure in the ‘SalesReport’ class is calculated by iterating through each product in the inventory and determining the sales for each product. The total sales is then the sum of the sales for all products.

Here's the relevant code from the ‘generate_report’ method:


class SalesReport:


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


Let's break down the key parts:

i. The method iterates through each product in ‘self.inventory.products.items()’.

ii. For each product, it calculates the quantity sold (‘sold_quantity’) by subtracting the current quantity (‘product.quantity’) from the initial quantity (‘product.initial_quantity’). This assumes that the `initial_quantity` represents the original quantity before any sales.

iii. If the ‘sold_quantity’ is greater than 0 (meaning some units of the product were sold), it calculates the sales for that product (‘sales’) by multiplying the ‘sold_quantity’ by the product's price (‘product.price’).

iv. The details of the sales for each product are printed, including the quantity sold and the total sales for that product.

v. The ‘total_sales’ variable accumulates the sales for all products.

vi. Finally, the method prints the total sales across all products.

So, the ‘total_sales’ variable keeps track of the cumulative sales amount for all products in the inventory, and it is printed at the end of the report.

<br>

3) What happens if you try to sell more products than are available in the inventory?
   
 If you try to sell more products than are available in the inventory, the ‘sell_product’ method in the ‘Inventory’ class will raise a ‘ValueError’ with the message "Product not available or insufficient quantity." This is because the method checks whether the specified product exists in the inventory and whether the quantity to be sold is greater than the available quantity.

Here's the relevant code from the ‘sell_product’ method:


class Inventory:


    def sell_product(self, product_name, quantity):
        if product_name in self.products and self.products[product_name].quantity >= quantity:
            self.products[product_name].quantity -= quantity
            return self.products[product_name].price * quantity
        else:
            raise ValueError("Product not available or insufficient quantity")

If the condition ‘product_name in self.products and self.products [product_name].quantity >= quantity’ evaluates to ‘False’, indicating that the product is not available or the quantity is insufficient, the method raises a ‘ValueError’.

For example, let's say you have an inventory with 100 units of "Apple," and you try to sell 120 units of "Apple." This would result in a ‘ValueError’  being raised with the specified message, indicating that the sale cannot be processed due to insufficient quantity.

<br>
   
4) How would you modify this system to handle different categories of products?
   
   i. Product Class Modification:
    The Product class is modified to include a new attribute called category.
  This modification allows each product to be associated with a specific   category.   
   class Product:
       def __init__(self, name, price, quantity, category):
           self.name = name
           self.price = price
           self.quantity = quantity
           self.category = category  # New attribute for product category

       def __str__(self):
           return f"{self.name} ({self.category}) - ${self.price} (Quantity: {self.quantity})"
   

ii. Inventory Class Modification:
   The Inventory class is modified to use a tuple (product_name, category) as a key in the products dictionary.
   When adding a product or selling a product, the combination of product name and category is used as a unique identifier.

  
   class Inventory:
       def __init__(self):
           self.products = {}

       def add_product(self, product):
           key = (product.name, product.category)  # Use a tuple as a key for both name and category
           if key in self.products:
               self.products[key].quantity += product.quantity
           else:
               self.products[key] = product

       def sell_product(self, product_name, category, quantity):
           key = (product_name, category)
           if key in self.products and self.products[key].quantity >= quantity:
               self.products[key].quantity -= quantity
               return self.products[key].price * quantity
           else:
               raise ValueError("Product not available or insufficient quantity")
   

iii. SalesReport Class Modification:
 The SalesReport class is modified to reflect the changes in product representation when generating the sales report.
  The loop now iterates over a tuple (product_name, category) and retrieves the corresponding product.

   
   class SalesReport:
       def __init__(self, inventory):
           self.inventory = inventory

       def generate_report(self):
           total_sales = 0
           print("Sales Report:")
           for (product_name, category), product in self.inventory.products.items():
               sold_quantity = product.initial_quantity - product.quantity
               if sold_quantity > 0:
                   sales = sold_quantity * product.price
                   print(f"{product_name} ({category}): Sold {sold_quantity}, Total Sales: ${sales}")
                   total_sales += sales
           print(f"Total Sales: ${total_sales}")
   


iv. Example Usage:
   The example usage at the end demonstrates adding products with different categories and selling products based on both name and category.

   
   inventory = Inventory()
   inventory.add_product(Product("Apple", 0.50, 100, "Fruit"))
   inventory.add_product(Product("Banana", 0.30, 150, "Fruit"))
   inventory.add_product(Product("Laptop", 800, 10, "Electronics"))

   try:
       revenue = inventory.sell_product("Apple", "Fruit", 20)
       print(f"Revenue from sale: ${revenue}")
   except ValueError as e:
       print(e)

   inventory.list_products()

   report = SalesReport(inventory)
   report.generate_report()
   

These modifications make the system more flexible by allowing products to be categorized, providing a better way to organize and handle different types of products.

full Code: 

class Product:
    def _init_(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.initial_quantity = quantity
        self.category = category  # New attribute for product category

    def _str_(self):
        return f"{self.name} ({self.category}) - ${self.price} (Quantity: {self.quantity})"


class Inventory:
    def _init_(self):
        self.products = {}

    def add_product(self, product):
        key = (product.name, product.category)  # Use a tuple as a key for both name and category
        if key in self.products:
            self.products[key].quantity += product.quantity
        else:
            self.products[key] = product

    def sell_product(self, product_name, category, quantity):
        key = (product_name, category)
        if key in self.products and self.products[key].quantity >= quantity:
            self.products[key].quantity -= quantity
            return self.products[key].price * quantity
        else:
            raise ValueError("Product not available or insufficient quantity")

    def list_products(self):
        for product in self.products.values():
            print(product)


class SalesReport:
    def _init_(self, inventory):
        self.inventory = inventory

    def generate_report(self):
        total_sales = 0
        print("Sales Report:")
        for (product_name, category), product in self.inventory.products.items():
            sold_quantity = product.initial_quantity - product.quantity
            if sold_quantity > 0:
                sales = sold_quantity * product.price
                print(f"{product_name} ({category}): Sold {sold_quantity}, Total Sales: ${sales}")
                total_sales += sales
        print(f"Total Sales: ${total_sales}")


# Example Usage
inventory = Inventory()
inventory.add_product(Product("Apple", 0.50, 100, "Fruit"))
inventory.add_product(Product("Banana", 0.30, 150, "Fruit"))
inventory.add_product(Product("Laptop", 800, 10, "Electronics"))

try:
    revenue = inventory.sell_product("Apple", "Fruit", 20)
    print(f"Revenue from sale: ${revenue}")
except ValueError as e:
    print(e)

inventory.list_products()

report = SalesReport(inventory)
report.generate_report()

   

### To be Submitted as a Pull Request

These questions should be answered by modifying the code in this repository. You can add new files, modify existing files, or do whatever you like. Make these changes all on one branch as part of a singe pull request. Each question should be answered in a separate commit. Feel free to code-split or code-merge as you see fit.

5. Can you implement a feature to restock products and reflect this in the sales report?

6. There is a holiday sale coming up. How would you alter this code so that we can have a discounted price without losing the original pricing? 

7. Currently this code has no “database”. Design a way to write the inventory to a file (txt or CSV or similar) and then also design a way to read inventory from a file. This will mean we can save or restore our inventory from a file. The format/name of the file is up to you.

8. Given 2 different database files, create a summary that explains any differences. In this example we can assume the inventory reports are from the same store, just at different times.
