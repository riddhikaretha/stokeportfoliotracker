# Stock Portfolio Tracker
# Author: Riddhi Karetha

from datetime import datetime

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

sorted_portfolio = sorted(
    portfolio.items(),
    key=lambda item: stock_prices[item[0]] * item[1],
    reverse=True
)

print("\n📈 Portfolio Summary (Sorted by Value):")
for stock, qty in sorted_portfolio:
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} | Price: ₹{price} | Qty: {qty} | Value: ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")
print(f"🕒 Generated on: {timestamp}")

# ✅ FIX HERE (encoding added)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Generated on: {timestamp}\n")
    file.write("-" * 40 + "\n")
    for stock, qty in sorted_portfolio:
        file.write(
            f"{stock} | Price: ₹{stock_prices[stock]} | "
            f"Qty: {qty} | Value: ₹{stock_prices[stock] * qty}\n"
        )
    file.write("-" * 40 + "\n")
    file.write(f"Total Investment: ₹{total_investment}")

print("\n✅ Portfolio saved successfully to portfolio.txt")
