'''
Exercise 1: Simple while loopsExercise 1: Simple while loops

1. Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

2. Write a program to keep asking for a number until you enter a negative number. At the end, print the average of all entered numbers.

3. Write a program to keep asking for a number until you enter a negative number. At the end, print the number of even number entered.
'''
Sum=0
total=0
evens=0

def printEXIT(a,b,c):
    print("Sum of all the number entered:",a)
    print("Average of all the number entered:",b)
    print("Number of even number entered:",c)
    exit()
    pass

while True:
    x=input("Enter A Number: ")
    total+=1
    print("You have entered:", x if float(x)>=0 else printEXIT(Sum,Sum/total,evens))
    Sum+=float(x)
    evens+=1 if float(x)%2==0 else 0
    pass