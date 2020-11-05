'''
Exercise 4:
Write a python script to print a right angle triangle composed of alternating 0s and 1s.. For
example:
>>> Input number of rows: 5
1
01
101
0101
10101
'''
row = int(input("Input number of rows: "))

for x in range(1,row+1):
    if x%2==0:
        print(int(x/2)*'01')
    else:
        print('1'+int(x/2)*'01')