# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📊 Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n📈 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} - Quantity: {qty}, Value: ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Optional file saving
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}, Quantity: {qty}, Value: ₹{stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}")
    print("✅ Portfolio saved to portfolio.txt")
