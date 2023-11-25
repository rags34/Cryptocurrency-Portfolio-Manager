from cp import Portfolio

obj = Portfolio()

def add_coin():
    #Asks the user for coin details and adds them to the portfolio.
    coin = input("Please enter the name of the Coin: ")
    amount = float(input("Please enter the Quantity: "))

    obj.add_coin(coin.lower(), amount)  # Convert coin name to lowercase for uniformity

while True:
    #Main program loop to provide options for user interaction.
    print("ACTIONS -> 1. View Portfolio   2. Add Coin   3. Total Valuation")
    action = input("Please enter the action (1-3) you want to perform (enter any other key to exit): ")

    if action == '1':
        # Show the current holdings in the portfolio
        obj.view_portfolio()

    elif action == '2':
        # Add a new coin to the portfolio
        add_coin()

    elif action == '3':
        # Show the total valuation of the portfolio
        val = obj.valuation()
        print(f"Total Portfolio Value: ${val:.2f}")

    else:
        # Exit the program if any other key is entered
        print("Keep Hodling, Have a nice day!")
        break
