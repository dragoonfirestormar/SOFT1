# For the three exerices, you should refactor the code you wrote in week 3

# 1- Write a function sum_all(n) that returns the sum of the first n positive 
# natural numbert. The function should return -1 if n<0.

def sum_all(n):
    if n < 0:
        return -1

    total = 0
    for value in range(n):
        total += value
    return total

number = 5
print('The sum of the first', number, 'natural number is:', sum_all(number))

# 2- Write a mul_table(n) that prints the multiplication table of the number n
# (see below). The function should print an error message if n<0.
# 1 x 3 = 3
# 2 x 3 = 6
# ...
# 10 x 3 = 30

# Note, you could have a much simpler implementation if you don't mind a messy table

# You should read the page about string formating at:
# https://realpython.com/python-formatted-output/
# to understand the code below

def mul_table(number):

    if number < 0:
        print("Error: the number should be a positive natural number!")

    number_length = len(str(number)) # value used to have a nice table formating
    table = ''
    for i in range(1, 11):
        table += '{0:>2d} x {1} = '.format(i, number) 
        # create formatting for the right hand side of the -= in table
        formatting =('{0:>' + str(number_length + 1) + 'd}\n')
        table += formatting.format(number * i)

    print(table)

mul_table(3) # calling/invoking the function mul_table


# 3- Write a function factorial(n) that returns n!. The function should return
# -1 if n < 0.

def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    return fact

n = 6
print(str(n) + '! =', factorial(n))
