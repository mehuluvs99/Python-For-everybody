
words = []

filename = input("Enter File Name: ")
fhand = open(filename, "r")

for line in fhand:
    for word in line.split(" "):
        if word not in words:
            words.append(word)


print(sorted(words))




