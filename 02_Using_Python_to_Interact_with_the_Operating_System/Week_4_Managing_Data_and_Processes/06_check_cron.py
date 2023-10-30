import sys
import re

# We will use the syslog.txt file for this example.
logfile = sys.argv[1]
usernames = {}


with open(logfile) as file:
    for line in file:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)

# $ python check_cron.py syslog.txt
# {'good_user': 1, 'naughty_user': 3}
