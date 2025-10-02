from pyscript import display
#Restaurant Ordering System using Python 

#String Data Type
restaurant_name = "Everything You Need"
owner_name = "GM Buhain"

#Integer Data Type
year_since = 2025

#Float Data Type
tax_rate = 0.08

#Boolean Data Type
has_delivery = True
is_dine_in = True
is_takeaway = False

#List Data Types
product_names = ["Cold Spaghetti", "Butterscotch Pie", "Cinnamon Pie", "Chocolate Bar"]
beverages = ["Water", "Sparkling Water"]

#Tuple Data Types
business_hours = ("1:00 AM", "12:00 PM")

#Disctionary Data Types
menu = {
    "Cold Spaghetti": 69.99,
    "Butterscotch Pie": 79.99,
    "Cinnamon Pie": 59.99,
    "Chocolate Bar": 150.00,
    "Water": 1.00,
    "Sparkling Water": 9.99
}

#Set Data Types
common_allergens = {"nuts", "dairy", "gluten"}

#Displaying Restaurant Information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

#Display menu items
display(product_names[0], target="product1")
display(f"₱{menu['Cold Spaghetti']:.2f}", target="price1")
display(product_names[1], target="product2")
display(f"₱{menu['Butterscotch Pie']:.2f}", target="price2")
display(product_names[2], target="product3")
display(f"₱{menu['Cinnamon Pie']:.2f}", target="price3")
display(product_names[3], target="product4")
display(f"₱{menu['Chocolate Bar']:.2f}", target="price4")
display(product_names[4], target="product5")
display(f"₱{menu['Water']:.2f}", target="price5")
display(product_names[5], target="product6")
display(f"₱{menu['Sparkling Water']:.2f}", target="price6")

#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openinghours")

#Display order type
display(f"Dine-in Available", target="orderType")