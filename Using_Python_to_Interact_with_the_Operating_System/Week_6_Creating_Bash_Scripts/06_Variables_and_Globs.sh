#!/bin/bash

# When creating a variable there cannot be spaces in between.
line="----------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"; echo

# Globs are characters that allow us to create list of files. 
# The star * and question mark ? are the most common Globs.
# Using these globs lets us create sequences of filenames that 
# we can use as parameters to the commands we call our scripts.

echo "this will show all the files that have the .py extension"; echo $line
echo "echo *.py"
echo *.py