'''
THE PROBLEM
A prime number (or a prime) is a natural number greater than 1 that has
no positive divisors other than 1 and itself.
The property of being prime is called primality. A simple but slow method of
verifying the primality of a given number is known as trial division. It
consists of testing whether is a multiple of any integer between 2 and√ .
'''

'''
THE BASIC
Write a program that, given a number comprised between 2 and 49, returns
if it is a prime number or not. We can assume that the computer knows
(stores) that [2, 3, 5, 7] are prime numbers.
'''

prime = [2,3,5,7]
print(prime)

input = int(input("Enter Your Number: "))

valid=True

for i in prime:
    if(input%i==0):
        valid=False
        pass
    pass

print(  'prime' if valid else 'non-prime' )