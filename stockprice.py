# Stock Portfolio Tracker
# Author: Riddhi Karetha

from datetime import datetime
import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📊 Available Stocks:")
for stock, price in stock_prices.items():
    print(f"- {stock}: ₹{price}")

# Input loop
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a valid positive number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Sort by value
sorted_portfolio = sorted(
    portfolio.items(),
    key=lambda item: stock_prices[item[0]] * item[1],
    reverse=True
)

print("\n📈 Portfolio Summary:")
for stock, qty in sorted_portfolio:
    price = stock_prices[stock]
    value = price * qty
    avg_price = value / qty
    total_investment += value

    print(
        f"{stock} | Qty: {qty} | "
        f"Avg Price: ₹{avg_price:.2f} | "
        f"Value: ₹{value}"
    )

print(f"\n💰 Total Investment Value: ₹{total_investment}")
print(f"🕒 Generated on: {timestamp}")

# Save TXT file
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Generated on: {timestamp}\n")
    file.write("-" * 50 + "\n")
    for stock, qty in sorted_portfolio:
        file.write(
            f"{stock} | Qty: {qty} | "
            f"Value: ₹{stock_prices[stock] * qty}\n"
        )
    file.write("-" * 50 + "\n")
    file.write(f"Total Investment: ₹{total_investment}")

# 🔹 CSV EXPORT (NEW)
with open("portfolio.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
    for stock, qty in sorted_portfolio:
        writer.writerow([
            stock,
            qty,
            stock_prices[stock],
            stock_prices[stock] * qty
        ])

print("\n✅ Portfolio saved to portfolio.txt and portfolio.csv")
