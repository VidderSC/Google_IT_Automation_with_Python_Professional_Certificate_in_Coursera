# Careful when opening a file using "w" as it will delete
# it's content as soon as it opens the file.
# If you want to append new lines to the file, you should
# use "a" instead of "w"

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy nigth.")

