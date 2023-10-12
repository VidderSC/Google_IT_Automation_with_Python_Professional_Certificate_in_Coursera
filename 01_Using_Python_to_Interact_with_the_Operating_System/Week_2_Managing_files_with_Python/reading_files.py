with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

print()

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

