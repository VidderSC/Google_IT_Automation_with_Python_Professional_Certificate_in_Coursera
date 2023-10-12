#!/bin/bash

# Clear the oldFiles.txt file
> oldFiles.txt

# Find files containing "jane" in list.txt and
# convert line endings to Unix format
files=$(grep ' jane ' ../data/list.txt | cut -d ' ' -f 3 | dos2unix)

for file in $files; do
    if [ -e "..$file" ]; then
        # appending the absolute paths to oldFiles.txt
        echo "$(realpath .."$file")" >> oldFiles.txt
    fi
done