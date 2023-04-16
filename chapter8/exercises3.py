
my_nums = []


while True:
    str_val = input("Enter a Number: ")
    if str_val == "done":
        break
    try:
        val = float(str_val)
    except:
        print("Invalid Input")
        continue

    my_nums.append(val)    

print("Minimun :",min(my_nums)," Maximum: ",max(my_nums))