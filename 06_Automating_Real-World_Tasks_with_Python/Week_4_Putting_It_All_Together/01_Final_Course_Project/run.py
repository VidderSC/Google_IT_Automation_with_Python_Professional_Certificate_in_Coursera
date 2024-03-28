#! /usr/bin/env python3

import os
import json
import requests


def process_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # We extract the information from the .txt file
        name = lines[0].strip()
        weight = int(lines[1].split()[0])
        description = ' '.join(lines[2:]).strip()

        # We generate the image name based on the filename
        image_name = os.path.splitext(os.path.basename(file_path))[0] + '.jpeg'

        # We store the extracted info in a dictionary
        product_info = {
            'name': name,
            'weight': weight,
            'description': description,
            'image_name': image_name
        }
        return product_info


def process_all_files(directory):
    products = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            # Process txt file and append its information to the products list
            product_info = process_text_file(file_path)
            products.append(product_info)
    return products


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def upload_to_server(products, server_url):
    for product in products:
        try:
            response = requests.post(server_url, json=product)
            # Raise an error for non-2xx status codes
            response.raise_for_status()
            print(f"Uploaded {product['name']} successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to upload {product['name']}: {e}")


if __name__ == "__main__":
    directory = "supplier-data/descriptions"
    server_url = "http://35.243.156.164/fruits"

    products = process_all_files(directory)
    save_to_json(products, 'products.json')

    upload_to_server(products, server_url)
