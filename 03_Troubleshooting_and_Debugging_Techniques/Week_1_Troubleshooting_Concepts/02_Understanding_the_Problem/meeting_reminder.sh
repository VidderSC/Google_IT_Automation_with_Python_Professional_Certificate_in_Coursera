#!/bin/bash

# 2.- We add the --forms-date-format line.
meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%Y-%m%d' \
    2>/dev/null)

# 1.- We add the echo to verify the info inside the variable.
echo $meeting_info
# The value is: 01/13/2020|Test|Amanda

if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
