filename = input("Enter File Name: ")
fhand = open(filename, "r")
count = 0

for line in fhand:
    if line.startswith("From:"):
        print(line.split(" ")[1])
        count += 1

print("There were ", count," lines in the file with From as the first word")