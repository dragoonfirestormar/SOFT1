'''
Exercise 1: Simple functionsExercise 1: Simple functions
Write a function sum_all(n) that returns the sum of the first n positive natural numbert. The function should return -1 if n<0.
Write a mul_table(n) that prints the multiplication table of the number n (see below). The function should print an error message if n<0.
  1 x 3 =   3
  2 x 3 =   6
  ...
10 x 3 = 30
Write a function factorial(n) that returns n!. The function should return -1 if n < 0.
'''
def sum_all(n):
    if n==0:
        return 0
    elif n<0:
        return -1
    else:
        return n+ sum_all(n-1)

def mul_table(n):
    if n<0:
        return 'error'
    else:
        table = ''
        for x in range(1,11):
            table+= f"{x} x {n} = {x*n}\n"
        return table

def factorial(n):
    if n==0: 
        return 1
    elif n<0:
        return -1
    else:
        return n* factorial(n-1)
    
print(sum_all(10))
print(mul_table(3))
print(factorial(10))