import re
filename = input("Enter the file name: ")
fhand = open(filename, "r")

num = []
for line in fhand:
    match = re.search("New\sRevision:\s(\d+)", line)
    if match:
        num.append(int(match.group(1)))

print(sum(num)/len(num))
