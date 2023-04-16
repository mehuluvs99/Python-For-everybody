filename = input("Enter File Name: ")
fhand = open(filename, "r")

hour_of_day = {}
email_addresses = {}
for line in fhand:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(":")[0]

        hour_of_day[hour] = hour_of_day.get(hour, 0) + 1


lst = list(hour_of_day.items())

#second mothod 
#for key, value in hour_of_day.items():
#    lst.append((key,value))
lst.sort()

for t in lst:
    print(t[0], t[1])

