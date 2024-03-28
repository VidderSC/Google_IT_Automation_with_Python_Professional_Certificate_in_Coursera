#!/usr/bin/env python3

import os
import datetime
import json
import reports
import emails


def load_from_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


def generate_paragraph(products):
    paragraph = ""
    for product in products:
        paragraph += f"name: {product['name']}<br/>weight: {product['weight']} lbs<br/><br/>"
    return paragraph


def main():
    json_file = "products.json"
    products = load_from_json(json_file)

    title = f"Processed Update on {datetime.datetime.now().strftime('%Y-%m-%d')}"

    paragraph = generate_paragraph(products)
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    email = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(email)


if __name__ == "__main__":
    main()
