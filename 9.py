"""
    Binary to Decimal Conversion
"""
x = int (input("Enter any number: "))
y = bin(x)
print("Binary Number : ",y.replace("0b",""))
print("Number into decimal : ",int(y,2))
