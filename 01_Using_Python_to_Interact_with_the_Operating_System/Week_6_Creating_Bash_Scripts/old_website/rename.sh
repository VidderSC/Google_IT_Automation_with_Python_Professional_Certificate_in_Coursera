#!/bin/bash

for file in *.HTM
do
    # We are surrounding our file variable with double-quotes to allow
    # the command to work even if the file has spaces in its name.
    name=$(basename "$file" .HTM)
    # We use echo to test first if our script works without modifying any files.
    # After we checked that it works as intended, we can remove the 
    # echo command to actually run the rename command.
    echo mv "$file" "$name.html"
done