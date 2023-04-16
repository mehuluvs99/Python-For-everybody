str = 'X-DSPAM-Confidence:0.8475'
print(str.find(":"))
col_index = str.find(":")
num = float(str[col_index+1:])
print(num)
print(type(num))


col_index2 = str.find("-")
num2 = str[col_index2+1:str.find(":")]
print(num2)
