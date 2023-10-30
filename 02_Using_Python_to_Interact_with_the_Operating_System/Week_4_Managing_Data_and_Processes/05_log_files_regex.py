import sys
import re

# We will use the syslog.txt file for this example.
logfile = sys.argv[1]

with open(logfile) as file:
    for line in file:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result[1])

# Returns:
# good_user
# naughty_user
# naughty_user
# naughty_user