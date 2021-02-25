# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


#SETUP
from datetime import datetime

subtotal = 0
entered_ids = []

#USER PROMPT
while True:
    entered_id = input("Please enter your product ID, or when finished, say DONE:")
    if entered_id == "DONE":
        break
    else:
        entered_ids.append(entered_id)

####NEED TO ADD DATA VALIDATION (Values between 1 and 20) WITH FRIENDLY USER ERROR PROMPT IF ENTERED INCORRECTLY

#WELCOME
print("**********************")
print("FARM TO TABLE GROCERY")
print("farmtotablegrocery.com | (202) 785-3002")
print("**********************")

#CURRENT TIME AND DATE
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y at %H:%M:%S")
print("CHECKOUT TIME: " + dt_string)
print("**********************")

#PRODUCT LIST WITH PRICES IN USD
for entered_id in entered_ids:
    chosen_products = [p for p in products if str(p["id"]) == entered_id]
    chosen_product = chosen_products[0]
    subtotal = subtotal + chosen_product["price"]
    product_price = "${:,.2f}".format(chosen_product["price"])
    print("PRODUCT: " + chosen_product["name"] + "....." + str(product_price))
print("**********************")

#SUBTOTAL
sub = "${:,.2f}".format(subtotal)
print("SUBTOTAL: " + str(sub))

#TAX
tax_rate = .0875
tax = float(subtotal) * tax_rate
taxes = "${:,.2f}".format(tax)
print("TAX: " + str(taxes))

#TOTAL
final_price = float(subtotal) + tax
total = "${:,.2f}".format(final_price)
print("TOTAL: " + str(total))

#BYE!
print("**********************")
print("Thanks for choosing Farm to Table Grocery!")
print("**********************")