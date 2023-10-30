import csv

hosts = [["workstation.local", "192.168.25.46"],
         ["webserver.cloud", "10.2.5.6"]]

# We need to add the 'newline=""' for it to not insert 
# a blank line between records on the created file.
with open("hosts.csv", "w", newline="") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
