
import csv

# Stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175
}

# Empty list to store portfolio
portfolio = []

# Function to display available stocks
def show_stocks():
    print("\nAvailable Stocks:")
    print("-------------------------")

    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

# Function to add stocks
def add_stock():
    show_stocks()

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return

            price = stock_prices[stock_name]
            investment = price * quantity

            portfolio.append({
                "Stock": stock_name,
                "Quantity": quantity,
                "Price": price,
                "Investment": investment
            })

            print("\nStock added successfully!")
            print("Investment Amount: $", investment)

        except ValueError:
            print("Please enter a valid quantity!")

    else:
        print("Stock not available!")

# Function to display portfolio
def show_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty!")
        return

    total = 0

    print("\n========== YOUR PORTFOLIO ==========")
    print("Stock\tQuantity\tPrice\tInvestment")
    print("-----------------------------------")

    for item in portfolio:
        print(
            f"{item['Stock']}\t"
            f"{item['Quantity']}\t\t"
            f"${item['Price']}\t"
            f"${item['Investment']}"
        )

        total += item["Investment"]

    print("-----------------------------------")
    print("Total Investment: $", total)

# Function to save portfolio in CSV file
def save_portfolio():
    if not portfolio:
        print("\nNo data available to save!")
        return

    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Stock", "Quantity", "Price", "Investment"]
        )

        writer.writeheader()
        writer.writerows(portfolio)

    print("\nPortfolio saved successfully in portfolio.csv!")

# Main menu
while True:

    print("\n================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("================================")
    print("1. Show Available Stocks")
    print("2. Add Stock")
    print("3. View Portfolio")
    print("4. Save Portfolio")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        add_stock()

    elif choice == "3":
        show_portfolio()

    elif choice == "4":
        save_portfolio()

    elif choice == "5":
        print("\nThank you for using Stock Portfolio Tracker!")
        break

    else:
        print("\nInvalid choice! Please try again.")