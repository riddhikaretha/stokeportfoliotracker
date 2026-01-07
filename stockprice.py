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
    stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        print("\n✅ Input completed.")
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n📈 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} - Quantity: {qty}, Value: ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")
