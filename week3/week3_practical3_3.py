''''
Exercise 3: from “Python Programming Fundamental”- Kent L, 2nd Ed. (2014)
There is an elegant algorithm for converting a decimal number to a binary number. You need
to carry out long division by 2 to use this algorithm. If we want to convert 8310 to binary then
we can repeatedly perform long division by 2 on the quotient of each result until the quotient
is zero. Then, the string of the remainders that were accumulated while dividing make up the
binary number. For example,
83/2 = 41 remainder 1
41/2 = 20 remainder 1
20/2 = 10 remainder 0
10/2 = 5 remainder 0
5/2 = 2 remainder 1
2/2 = 1 remainder 0
1/2 = 0 remainder 1
The remainders from last to first are 10100112 which is 8310. This set of steps is called an
algorithm. An algorithm is like a recipe for doing a computation. We can use this algorithm
any time we want to convert a number from decimal to binary.
Implement a script that prompts the user to enter a positive in and print a binary representation
of that number
'''
num = int(input("Enter the number: "))

statement = ''
while num/2!=0 :
    statement += str(num%2)
    num=int(num/2)

print(statement[::-1]) 