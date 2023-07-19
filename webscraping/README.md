# Web Scraping in Python: Google Finance Most Active Stocks

This is a Python script that performs web scraping on the Google Finance page to obtain information about the most active stocks in real-time. The script extracts data such as company name, stock symbol, share price, and the rate of change in percentage, and stores them in a dictionary.

## Usage

1. Clone this repository to your local machine:
   git clone https://github.com/Jampierss/Python-scripts/webscraping.git

2. Navigate to the script's folder:
   cd repository_name

3. Run the script from the command line:
   python script_name.py

## Requirements

- Python 3.x
- Libraries: requests, BeautifulSoup

You can install the required libraries with the following command:
  pip install requests beautifulsoup4

## Results

The script makes an HTTP request to the Google Finance page that displays the most active stocks. It then parses the HTML content using BeautifulSoup and extracts relevant data such as the company name, stock symbol, share price, and the rate of change in percentage. The data is stored in a dictionary, which is saved in a JSON file named "Markets_shares.json".

## Contributions

If you'd like to contribute to this project, you're welcome to do so! You can submit your improvements, bug fixes, or suggestions via pull requests. Please make sure to follow the contribution guidelines outlined in the CONTRIBUTING.md file.

## Contact

If you have any questions or comments, feel free to contact me at jimmyflorian2005@gmail.com or open an issue in this repository.

I hope this script proves useful for your web scraping projects in Python!
