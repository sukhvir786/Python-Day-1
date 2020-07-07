"""
    octal to Decimal Conversion
"""
x = int (input("Enter any number: "))
y = oct(x)
print("octal Number : ",y.replace("0o",""))
print("Number into decimal : ",int(y,8))
