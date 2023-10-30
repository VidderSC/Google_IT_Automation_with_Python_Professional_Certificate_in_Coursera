import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    print("On Windows Powershell, use $LASTEXITCODE to see the exit code number.")
    sys.exit(1)
