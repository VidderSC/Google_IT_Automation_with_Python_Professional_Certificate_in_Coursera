#!/bin/bash

# In Bash scripting, an exit value of 0 means success.
clear

if grep "127.0.0.1" /etc/hosts; then
    echo
    echo "Everything is ok"
else
    echo
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

echo

# Test: A command that evaluates the conditions received
# and exits with zero when they are true and with one
# when they are false.

if test -n "$PATH"; then echo "Your PATH is not empty"; fi
echo

# An alias of the test command would be using [ ],
# There must be a space before the closing bracket.

if [ -n "$PATH" ]; then echo "Your PATH is not empty"; fi

echo
echo "The screen will clear after 5 seconds"
echo "because I used the 'sleep 5s' command to wait that amount of time"
echo "and the clear command to clean the screen."

sleep 5s
clear