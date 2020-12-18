'''
Exercise 2: from “Python Programming Fundamental”- Kent L, 2nd Ed. (2014)
There is an elegant algorithm for converting a decimal number to a binary number. You need
to carry out long division by 2 to use this algorithm. If we want to convert 8310 to binary, then
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
The remainders from last to first are 10100112 which is 8310.
a) Implement a recursive function to_binary(number) that takes a positive integer
as parameter and returns a binary representation of that number as a string.
b) Implement the reverse function to_base10(binary) that takes a string containing
a binary number and returns its representation in base 10. The function must be
recursive. To test your solution once implemented to_base10(to_binary(83))
should return 83
'''

# base 10 to base 2
def to_binary(number):
    if number == 0:
        return str()
    if number%2==0:
        return to_binary(int(number/2)) + str(0)
    else:
        return to_binary(int(number/2)) + str(1)

print(to_binary(83))


###########################################################


# base 2 to base 10
def to_base10(number):
    if number=='':
        return 0
    return int(number[0])*2**(len(number)-1) + to_base10(number[1:])

print(to_base10('1010011'))
