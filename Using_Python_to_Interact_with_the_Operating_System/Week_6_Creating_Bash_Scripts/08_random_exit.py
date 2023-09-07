#!/usr/bin/env python3

# This script simply generates a random number between 0 and 3 and
# we pass that value to the sys.exit command to return that as an
# exit value of our program.

import sys
import random

value = random.randint(0, 3)

print("Returning: " + str(value))

sys.exit(value)
