import os
from datetime import datetime

file1 = "novel.txt"
file2 = "first_draft.txt"
file3 = "finished_masterpiece.txt"

if os.path.exists(file1):
    os.remove(file1)
else:
    print(f'File "{file1}" does not exist.')

print()

if os.path.exists(file2):
    os.rename(file2, file3)
else:
    print(f'File "{file2}" does not exist.')

print()

print(os.path.exists(file1))
print(os.path.exists(file2))
print(os.path.exists(file3))

print()

file4 = "spider.txt"
size = os.path.getsize(file4)
modified_time = os.path.getmtime(file4)

print(os.path.abspath(file4))
print(f"The size of '{file4}' is {size} bytes")
print(f"and the modified time is {modified_time} (Timestamp)")

timestamp = datetime.fromtimestamp(modified_time)
print(f"Which is {timestamp}")
