products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
#list of the prices and quantities sold over last week
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products
total_price_average = sum(prices) / len(prices)
print("Total Price Average:", total_price_average)

# Create a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Calculate the total revenue generated from the products
total_revenue = sum(price * quantity for price, quantity in zip(prices, last_week))
print("Total Revenue:", total_revenue)

# Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / len(last_week)
print("Average Daily Revenue:", average_daily_revenue)

# Find products with prices less than $30 based on the new prices
less_than_30 = [product for product, price in zip(products, new_prices) if price < 30]
print("Products with Prices Less than $30:", less_than_30)
