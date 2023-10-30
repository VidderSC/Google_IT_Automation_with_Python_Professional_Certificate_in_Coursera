#!/usr/bin/env python3

import re
import csv
import sys

errors_dict = {}
users_dict = {}
lines = []

try:
    with open("syslog.log", "r") as file:
        lines = file.readlines()
except FileNotFoundError as e:
    print(f"Syslog File not found, with error: {e}")
    sys.exit(1)

error_pattern = r"ticky: (ERROR [\w \']*) \(([a-z.]*)\)"
info_pattern = r"ticky: (INFO [\w \']*) \[#[0-9]*\] \(([a-z.]*)\)"

for line in lines:
    error_result = re.search(error_pattern, line)
    info_result = re.search(info_pattern, line)

    if info_result is not None:
        log, user = info_result.groups()
    elif error_result.groups() is not None:
        log, user = error_result.groups()

    if user not in users_dict:
        users_dict[user] = {"INFO": 0, "ERROR": 0}

    if "INFO" in log:
        users_dict[user]["INFO"] += 1

    if "ERROR" in log:
        users_dict[user]["ERROR"] += 1
        clean_log = re.sub(r"^ERROR\s+", "", log)
        if clean_log not in errors_dict:
            errors_dict[clean_log] = 1
        else:
            errors_dict[clean_log] += 1

csv_errors = "error_message.csv"
csv_users = "user_statistics.csv"

sorted_users_dict = dict(sorted(users_dict.items()))
sorted_errors_dict = dict(
    sorted(errors_dict.items(), key=lambda item: item[1], reverse=True))

with open(csv_users, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])

    for username, counts in sorted_users_dict.items():
        writer.writerow([username, counts.get(
            "INFO", 0), counts.get("ERROR", 0)])

print(f"Data exported to {csv_users}")

with open(csv_errors, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])

    for error_type, count in sorted_errors_dict.items():
        writer.writerow([error_type, count])

print(f"Data exported to {csv_errors}")
