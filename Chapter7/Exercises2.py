filename = input("Enter  the file name: ")
fhand = open(filename, "r")


count = 0
total_confidence = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        space_index = line.find(" ")
        my_num = float(line[space_index+1:])
        total_confidence += my_num
        count += 1



print("average spam confidence:" , total_confidence/count)