filename = input("Enter File Name: ")
fhand = open(filename, "r")

email_addresses = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1
max_address = None
max_email = 0
for k in email_addresses:
    if email_addresses[k] > max_email:
        max_address = k
        max_email = email_addresses[k]

print(max_address, max_email)