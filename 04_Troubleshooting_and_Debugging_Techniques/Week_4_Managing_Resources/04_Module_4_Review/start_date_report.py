#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

data_dict = None

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    global data_dict
    
    if data_dict is None:
        data = get_file_lines(FILE_URL)
        reader = csv.reader(data[1:])

        data_dict = {}

        for row in reader:
            row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
            if row_date not in data_dict:
                data_dict[row_date] = []
            data_dict[row_date].append(f"{row[0]} {row[1]}")
    
    closest_dates = []
    for date in sorted(data_dict.keys()):
        if date >= start_date:
            closest_dates.append(date)

    if closest_dates:
        closest_date = closest_dates[0]
        employees = data_dict[closest_date]
        return closest_date, employees
    else:
        closest_date = datetime.datetime.today()
        return closest_date, []

def list_newer(start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
