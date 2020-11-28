'''
Exercise 1:
1. Write a script asking the user to enter a series of positive integers separated by a white
space, and then prints the number of even numbers that was entered. For example:
>>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
There are 6 even numbers
You will need to use the built-in function input() and the string method split().
You should also remember that we can convert a string representing an integer into an
int like so:
>>> twenty = int('20')
>>> type(twenty)
<class 'int'>
2. Same question except we would like to have the list of even number as well
>>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
There are 6 even numbers: 2 4 6 8 2 100
3. Same question except we would like to have the list of even number without duplicate,
that is remove the second 2 in the example below.
>>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
There are 5 distinct even numbers: 2 4 6 8 100
'''
def even(x):
    return ( True if x%2==0 else False )

values = str(input('Enter numbers: ')).lower().strip()

counter=0
num = ''
listEven = ''
disEven = []
for x in values:
    if x==' ':
        val = int(num)
        if(even(val)):
            disEven.append(num)
            counter+=1
            listEven += num+","
        num = ''
    if(x>='0' and x<='9'):
        num += x

print('There are ',counter,' even numbers:')
print(listEven[:-1]+'\n')
disEven = list(dict.fromkeys(disEven))
print('There are ',len(disEven),' distinct even numbers:')
tempString = ''
for x in disEven:
    tempString+=x+","

print(tempString[:-1])