count = 0


while True:
    str_val = input("Enter a Number: ")
    if str_val == "done":
        break
    try:
        val = float(str_val)
    except:
        print("Invalid Input")
        continue

    if count == 0:
        min_val = val
        max_val = val
    elif val < min_val:
        min_val = val
    elif val > max_val:
        max_val = val

    count = count + 1

print("minimum value :",min_val , "Maximum value :",max_val)   
#print("Total sum of Number: ",total,"Total Count Of number: ", count, "Total divided count :",total/count)