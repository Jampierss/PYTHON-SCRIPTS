# Web Scraping in Python: Google Finance Most Active Stocks

This is a Python script that performs web scraping on the Google Finance page to obtain information about the most active stocks in real-time. The script extracts data such as company name, stock symbol, share price, and the rate of change in percentage, and stores them in a dictionary.

## Usage

1. Clone this repository to your local machine:
   <code>git clone https://github.com/Jampierss/Python-scripts.git</code>

2. Navigate to the script's folder:
   <code>cd Python-scripts/webscraping</code>

3. Run the script from the command line:
   <code>python stocks.py</code>

## Requirements

- Python 3.x
- Libraries: requests, BeautifulSoup

You can install the required libraries with the following command:
  <code>pip install requests beautifulsoup4</code>

## Results

The script makes an HTTP request to the Google Finance page that displays the most active stocks. It then parses the HTML content using BeautifulSoup and extracts relevant data such as the company name, stock symbol, share price, and the rate of change in percentage. The data is stored in a dictionary, which is saved in a JSON file named "Markets_shares.json".

## Contact

If you have any questions or comments, feel free to contact me at jimmyflorian2005@gmail.com or open an issue in this repository.

I hope this script proves useful for your web scraping projects in Python!
