"""
    Conversion from decimal to
    binary, octal and hexadecimal
"""
x = int (input("Enter any number: "))
y = x
z = x
x = bin(x).replace("0b","")
print("Number in binary:",x)
y = oct(y).replace("0o","")
print("Number in octal:",y)
z = hex(z).replace("0x","")
print("Number in hexadecimal:",z)
