'''
Exercise 1:
Write a function sum_digits(number) to calculate and return the sum of the digits of a
given whole number (int) given as parameter. For example,
>>> print(sum_digits(1234))
10
'''
def sum_digits(n):
    if len(str(n))==1:
        return n
    return int(str(n)[0]) + sum_digits(int(str(n)[1::]))

print(sum_digits(abs(int(input('Enter Your Number: ')))))
