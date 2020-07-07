"""
    hexadecimal to Decimal Conversion
"""
x = int (input("Enter any number: "))
y = hex(x)
print("hexadecimal Number : ",y.replace("0x",""))
print("Number into decimal : ",int(y,16))