try:
    hour = int(input("Enter Hour:\n"))
    rate = float(input("Enter Rate:\n"))
    pay = hour * rate

    if hour > 40:
        pay = (hour - 40)*rate*1.5+40*rate
    else:
        pay = hour * rate
    print("Pay: ", pay)

except:
    print("Error !, Please Enter Proper Numberical Inpur")