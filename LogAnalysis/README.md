# Log Analysis Script

This script is designed to analyze a syslog log file and generate two CSV files, one for error messages and another for user statistics.

## Prerequisites

- Python 3

## Usage

1. Place the `syslog.log` file containing the log data in the same directory as this script.

2. Run the script using the following command:

   ```bash
   python3 script.py
3. The script will generate two CSV files: `error_message.csv` and `user_statistics.csv`.

## Script Explanation

The script performs the following steps:

1. Imports necessary modules for regular expressions and CSV handling.

2. Initializes dictionaries to store error and user statistics.

3. Reads each line of the `syslog.log` file and extracts relevant information using regular expressions.

4. Updates the dictionaries with error and user information based on the log lines.

5. Sorts the error dictionary based on the error message count in descending order.

6. Writes the sorted error dictionary to `error_message.csv` file.

7. Sorts the user dictionary and writes user statistics to `user_statistics.csv` file.

## Output

- `error_message.csv`: Contains a list of unique error messages and their corresponding counts in descending order.

- `user_statistics.csv`: Contains a list of usernames along with the count of INFO and ERROR messages associated with each user.

## Author

Created by `Jimmy Florian`

For any questions or issues, please contact `jimmyflorian2005@gmail.com`.
