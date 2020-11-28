'''
Exercise 2: simple for loopsExercise 2: simple for loops: 
1. Write a program that prompts the user to input a positive integer N and print the sum of the first N natural numbers.

2. Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number.

3. Write a program to print the factorial value of any number entered through the keyboard. You must use a for loop, not any math function that already exists.
'''
N=int(input("Enter The Number: "))
firstnsum=0
table="\n"
factorial=1
for x in range(1,N+1,1):
    firstnsum+=x
    table+=str(N)+"x"+str(x)+"="+str(N*x)+"\n"
    factorial*=x
    pass

print("Sum of first N digits: ",firstnsum)
print("Table: ",table)
print("Factorial: ",factorial)