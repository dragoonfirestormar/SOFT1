'''
Exercise 5:
Write a script that takes the lengths of the sides of a triangle (a, b, and c) from the user and then
print the area of the triangle using Heron's formula. (Look up Heron's formula if you do not
remember it.). Note, to compute 𝑥𝑥𝑛𝑛 using Python, you must use the function pow(x,n).
'''

a=float(input('Enter First Side: '))
b=float(input('Enter Second Side: '))
c=float(input('Enter Third Side: '))

s=(a+b+c)/2

print('Area Is', pow(((s*(s-a)*(s-b)*(s-c))), 1/2 ) )