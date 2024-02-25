#!/usr/bin/env python3

import json
import locale
import sys
import os
import reports
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.
    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    car_year_count = {}
    most_popular_year = data[0]["car"]["car_year"] if data else None

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price

        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        # TODO: also handle most popular car_year
        car_year = item["car"]["car_year"]
        car_year_count[car_year] = car_year_count.get(
            car_year, 0) + item["total_sales"]

        # Update most_popular_year
        if most_popular_year is None or car_year_count[car_year] > car_year_count.get(most_popular_year, 0):
            most_popular_year = car_year

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(
            most_popular_year, car_year_count[most_popular_year])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(
            item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)

    # Sort the list of cars by total sales
    data.sort(key=lambda car: car["total_sales"], reverse=True)

    # Generate PDF report
    pdf_path = "/tmp/cars.pdf"
    table_data = cars_dict_to_table(data)
    reports.generate(pdf_path, "Sales summary for last month", "<br/>".join(summary), table_data)

    # Send email with the generated PDF report
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = "\n".join(summary)
    message = emails.generate(sender, receiver, subject, body, pdf_path)
    emails.send(message)

    print(summary)


if __name__ == "__main__":
    main(sys.argv)
