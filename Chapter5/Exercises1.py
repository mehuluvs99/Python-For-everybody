count = 0
total = 0

while True:
    str_val = input("Enter a Number: ")
    if str_val == "done":
        break
    try:
        val = float(str_val)
    except:
        print("Invalid Input")
        continue

    total = total + val
    count = count + 1

print("Total sum of Number: ",total,"Total Count Of number: ", count, "Total divided count :",total/count)