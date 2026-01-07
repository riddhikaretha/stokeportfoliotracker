# Stock Portfolio Tracker

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
        print("❌ Quantity must be a positive number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n📈 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} | Price: ₹{price} | Qty: {qty} | Value: ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")
