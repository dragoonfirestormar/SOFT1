'''
Exercise 3:
Write a function to_base10(binary) that take a binary number (base 2), convert it into
a decimal number (base 10) and return the base 10 value. To compute such a value, we need to
understand what a binary number is.
Index 7 6 5 4 3 2 1 0
Binary 1 0 0 0 1 0 1 1
Decimal
139
1 × 2
7 0 × 2
6 0 × 2
5 0 × 2
4 1 × 2
3 0 × 2
2 1 × 2
1 1 × 2
0
128 0 0 0 8 0 2 1
The binary number 10001011 represents the number 139, whereas the number 11111111
represents 255.
'''
import math
def to_base10(binary):
    strBinReved = str(binary)[::-1]
    index = 0
    decimal = 0
    for x in strBinReved:
        decimal+=int(x)*math.pow(2,index)
        index+=1
    return decimal

print(to_base10(11111111))