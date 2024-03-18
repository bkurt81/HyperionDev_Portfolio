"""
- Create a list called menu, which should contain at least four items
- Create a dictionary called stock, which should contain the stock value for each item
- Create another dictionary called price, which should contain the prices for each item
- Calculate the total_stock worth in the cafe
- Finally, print out the result of your calculation

"""

# Create a list of menu items
menu = ["Coffee", "Tea", "Croissant", "Muffin", "Sandwich"]

# Create a dictionary to store stock for each item
stock = {
    "Coffee": 100,
    "Tea": 100,
    "Croissant": 50,
    "Muffin": 50,
    "Sandwich": 75
}

# Create a dictionary to store prices for each item
price = {
    "Coffee": 3.5,
    "Tea": 2.5,
    "Croissant": 1.75,
    "Muffin": 2.0,
    "Sandwich": 5.0
}

# Calculate the total stock worth
# Create a variable and set its value to 0
total_stock_worth = 0

# Loop through the menu list
for items in menu:
    # Calculate the value of each item in stock
    item_value = stock[items] * price[items]
    # Add the item value to the total stock worth
    total_stock_worth += item_value

# Print the result
print(f"The total stock worth in the cafe is: £{total_stock_worth:.2f}")
