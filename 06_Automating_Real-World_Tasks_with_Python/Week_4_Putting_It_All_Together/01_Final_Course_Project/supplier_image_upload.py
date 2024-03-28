#!/usr/bin/env python3

import os
import requests

url = "http://35.243.156.164/upload/"
source_folder = 'supplier-data/images'

# We list only JPEG files in the source folder
files = [file for file in os.listdir(source_folder) if file.endswith('.jpeg')]

# We Iterate over each file and upload them if they are .jpeg
for filename in files:
    file_path = os.path.join(source_folder, filename)
    with open(file_path, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

    # We check if the upload was successful
    if r.status_code == 201:
        print(f"Uploaded {filename} successfully")
    else:
        print(f"Failed to upload {filename}. Status code: {r.status_code}")
