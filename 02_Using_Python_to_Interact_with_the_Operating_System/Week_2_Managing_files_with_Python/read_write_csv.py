import csv

with open("software.csv") as soft:
    reader = csv.DictReader(soft)
    for row in reader:
        print(f"{row['name']} has {row['users']} users.")


users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion",
             "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]
with open("by_department.csv", "w", newline="") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
