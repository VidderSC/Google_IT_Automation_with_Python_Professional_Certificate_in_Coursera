#!/usr/bin/env python3

import sys
import subprocess

# We initialize the lists for source and destination paths
source_paths = []
dest_paths = []

# We check if we have received the file as an argument, if not
# we output a message and exit with an error
if len(sys.argv) != 2:
    print("Missing input file.")
    print("Usage: python3 changeJane.py input_file")
    sys.exit(1)

# We read the input file and populate the previous lists
with open(sys.argv[1]) as file:
    paths = file.readlines()

    for path in paths:
        # We remove the whitespaces at the beginning and ending of the string
        source_paths.append(path.strip())
        # We also replace the text "jane" with "jdoe"
        dest_paths.append(path.strip().replace("jane", "jdoe"))

# We loop through the pairs of the source and destination lists
for source, dest in zip(source_paths, dest_paths):
    # We use a try except block to make sure it can be renamed
    try:
        # We execute the mv command with each source and destination on the lists.
        # The "check=True" will return a non 0 exit status and raise an exception.
        subprocess.run(["mv", source, dest], check=True)
        # We print a message for each file that is renamed to see the progress.
        print("Renamed '{}' to '{}'".format(source, dest))
    except subprocess.CalledProcessError as e:
        print("Error renaming '{}' to '{}': {}".format(source, dest, e))
