#! /usr/bin/env python3

import os
import requests

# feedback_dir = os.path.join("/", "data", "feedback")
feedback_dir = os.path.join("data", "feedback")

# Obtain the list of all txt files in the feedback_dir
feedback_list = os.listdir(feedback_dir)
files = [os.path.join(feedback_dir, item) for item in feedback_list]

# Traverse over each file in files and create dictionary
data_dict_list = []

for file in files:
    with open(file) as f:
        lines = f.readlines()

    file_data = {
        'title': lines[0].strip(),
        'name': lines[1].strip(),
        'date': lines[2].strip(),
        'feedback': lines[3].strip(),
    }

    data_dict_list.append(file_data)

# use the request module to post the dictionary to the website.
# use requests.post() to make a POST request to f"http://{ip}/feedback"
url = "http://35.192.114.187/feedback/"

for data in data_dict_list:
    # make a POST request
    response = requests.post(url, json=data)

    # check for errors
    if response.status_code == 201:
        print(f"Data posted successfully for {data['name']}")
    else:
        print(
            f"Error posting data for {data['name']}. Status Code: {response.status_code}, Response Text: {response.text}")
