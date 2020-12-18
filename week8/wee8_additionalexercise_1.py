'''
Exercise 1:
1. Write a recursive function print_all(numbers) that prints all the
elements of list of integers, one per line (use no while loops or for loops).
The parameters numbers to the function is a list of int.
2. Same problem as the last one but prints out the elements in reverse order.
'''


#printing all in same order
def print_all(number):
    if len(number) <= 1:
        print (number[0])
    else:
        print (number[0])
        return print_all(number[1:])

print_all([1,2,3,4,5,6,7,8])


##############################################
print()
##############################################


#printing all in reverse order
def print_all_reverse(number):
    if len(number) <= 1:
        print (number[-1])
    else:
        print (number[-1])
        return print_all(number[:-1])

print_all_reverse([1,2,3,4,5,6,7,8])