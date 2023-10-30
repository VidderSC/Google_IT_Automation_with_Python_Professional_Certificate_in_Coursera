#!/bin/bash

clear

if [ -r "error_message.csv" ]; then
    echo "ERROR File exists and"
    # For Windows use:
    python csv_to_html.py error_message.csv error-counts.html
    
    # For Linux use:
    # ./csv_to_html.py error_message.csv /var/www/html/error-counts.html
else
    echo "ERROR File not found"
fi

echo 

if [ -r "user_statistics.csv" ]; then
    echo "USERS File exists and"
    # For Windows use:
    python csv_to_html.py user_statistics.csv users-counts.html
    
    # For Linux use:
    # ./csv_to_html.py user_statistics.csv /var/www/html/users-counts.html
else
    echo "USERS File not found"
fi
