

def computerpay (hour,rate):

    if hour > 40:
        pay = (hour - 40)*rate*1.5+40*rate
    else:
        pay = hour * rate
    return pay
hour = int(input("Enter Hour:\n"))
rate = float(input("Enter Rate:\n"))
pay= computerpay(hour,rate)

print("Pay: ", pay)