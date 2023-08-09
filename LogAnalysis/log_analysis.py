#!/usr/bin/env python3

import re
import csv

errorDic = {}
userDic = {}

with open("syslog.log", "r") as file:
        for line in file:
                match = re.search(r"\((\w+(?:\.\w+)?)\)$", line)

                if match:
                        username = match.group(1)

                        if username not in userDic:
                                userDic[username] = {"INFO": 0, "ERROR":0}

                        if "ERROR" in line:
                                userDic[username]["ERROR"]+= 1
                                err = re.search(r"ERROR\s+(.*?)(?:\s+\(.*\))?$", line)
                                error_message = err.group(1)
                                if error_message in errorDic:
                                        errorDic[error_message] += 1
                                else:
                                        errorDic[error_message] = 1
                        elif "INFO" in line:
                                userDic[username]["INFO"] += 1


errorDic = sorted(errorDic.items(), key=lambda item: item[1], reverse=True)
userDic = sorted(userDic.items())

with open("error_message.csv", "w", newline="") as error_csv:
        csv_writer = csv.writer(error_csv)
        csv_writer.writerow(["Error", "Count"])
        for username, count in errorDic.items():
                csv_writer.writerow([username, count])

# Store sorted user dictionary in user_statistics.csv
with open("user_statistics.csv", "w", newline="") as user_csv:
        csv_writer = csv.writer(user_csv)
        csv_writer.writerow(["Username", "INFO", "ERROR"])
        for username, data in userDic.items():
                csv_writer.writerow([username, data["INFO"], data["ERROR"]])
