import csv

file = open("csv_file.txt")
csv_file = csv.reader(file)

for row in csv_file:
    name, phone, role = row
    print(f"Name: {name}, Phone: {phone}, Role: {role}")

file.close()
