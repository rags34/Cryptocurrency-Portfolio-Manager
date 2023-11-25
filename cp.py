import requests
from bs4 import BeautifulSoup

def get_coin_info(coin):
    # Fetch the CoinMarketCap page for the specified coin
    res = requests.get(f"https://coinmarketcap.com/currencies/{coin}/")
    
    # If the request is successful (status code 200), proceed to scrape the price
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        # Find the element containing the price of the coin
        raw_price = soup.find('span', class_="sc-f70bb44c-0 jxpCgO base-text").text
        # Extract and format the price as a float
        price = float(raw_price.replace('$', '').replace(',', ''))
        return price  # Return the extracted price
    
    return None  # If the request failed or the coin doesn't exist, return None

class Portfolio:
    #A class to manage cryptocurrency holdings.
    def __init__(self):
        #Initializes an empty dictionary to store coin holdings.
        self.holdings = {}

    def add_coin(self, coin, amount):
        if(get_coin_info(coin)):
            # Add or update the coin and its amount in the portfolio
            if coin in self.holdings:
                self.holdings[coin] += amount
            else:
                self.holdings[coin] = amount
        else:
            print("Sorry, coin not in database")  # If the coin isn't found, inform the user

    def valuation(self):
        #Calculates the total valuation of the portfolio based on current prices.
        total_value = 0
        # Calculate the total value of the portfolio based on coin amounts and their prices
        for coin, amount in self.holdings.items():
            price = get_coin_info(coin)  # Fetch the current price of the coin
            if price:
                total_value += price * amount  # Calculate the total value of the coin holdings
        
        return total_value  # Return the total portfolio value

    def view_portfolio(self):
        #Displays the current holdings and their values in the portfolio.
        if self.holdings.items():
            # Display the current holdings in the portfolio along with their values
            for coin, amount in self.holdings.items():
                price = get_coin_info(coin)  # Get the current price of the coin
                total = price * amount  # Calculate the total value of the coin holding
                print(f"Coin: {coin}         Price: ${price}         Quantity: {amount}         Total Amount: ${total:.2f}")
        else:
            print("Portfolio is currently empty")  # If the portfolio is empty, inform the user
