import re
filename = input("Enter the file name: ")
regex = input("Enter a Regular Expression: ")
counter = 0
fhand = open(filename, "r")
for line in fhand:
    line = line.rstrip()
    if re.search(regex,line):
        counter += 1

print(counter)