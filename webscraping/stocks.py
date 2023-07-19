# Author: Jimmy Florian Tucta 

import requests
import json
from bs4 import BeautifulSoup

def scrape_sctocks():
    
    """
    Perform web scraping on the Google Finance page to obtain information about most active stocks in real time.

    Returns:
        dict: A dicctionary that contains data (NAME, SYMBOL, PRICE and RATE) about most active stocks in Google Finance page.

    Raises:
        Exception: If the page cannot be accessed or an error ocurrs in the HTTP request.
    """

    # Make a request
    url = "https://www.google.com/finance/markets/most-active"
    response = requests.get(url)

    # Throw an exception if the request was unsuccessful
    if response.status_code != 200:
        raise Exception(f"No se cargo la url: {response.status_code}")

    # Analize the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html5lib")

    # List to store data
    name_lst = []
    symbol_lst = []
    price_lst = []
    percent_lst = []

    # Find and extract company names
    for name in soup.find_all(class_="ZvmM7"):
        name_lst.append(name.text)

    # Find and extract stock symbols
    for symbol in soup.find_all(class_="COaKTb"):
        symbol_lst.append(symbol.text)
    
    # Find and extract share prices
    for price in soup.find_all(class_="YMlKec"):
        price_lst.append(price.text)

    # Find and extract rates of change in percent
    for rate in soup.find_all(class_="xVyTdb NN5r3b"):
        percent_lst.append(rate.span.get("aria-label"))
    
    # print(len(name_lst)) # 50
    # print(len(symbol_lst)) # 50 + 18
    # print(len(price_lst)) # 50 + 28
    # print(len(percent_lst)) # 50

    # Remove unnecessary data
    symbol_lst = symbol_lst[:-18]
    price_lst = price_lst[10:-18]

    # Create a dictionary to store stock data
    stock_data = {}
    for i in range(len(symbol_lst)):
        stock_data[symbol_lst[i]] = {
            "Name": name_lst[i],
            "Price": price_lst[i],
            "Rate": percent_lst[i]
        }
    
    return stock_data

def save_to_json(data, filename):
    """
    Save the data in a json file.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    try:
        stock_data = scrape_sctocks()
        file_name = "Markets_shares.json"
        save_to_json(stock_data, file_name)
        print(f"[+] The data has been successfully extracted and saved in {file_name}")
    except Exception as e:
        print(f"[-] Something went wrong!!! :( {e}")


        
