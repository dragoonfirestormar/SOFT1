'''
Exercise 2:
The aim of this exercise is to draw a sudoku board (not to solve it). To start with we will be
using a 4 × 4 board (as opposed to the classic 9 × 9).
1. Write a script that asks a user to enter 4 digits (comprised between 0 and 4) separated
by a white space, the store each digit in a list and print the list.
>>> enter 4 digits (0..4) separated by a space: 0 2 1 4
[0, 2, 1, 4]
2. Write a script that ask a user to enter 4 times a sequence of 4 digits, and store it in a 2D
list, that is a list containing 4 lists of 4 digits each. The script should print the 2D list.
The output should look like:
[[0,2,1,4],[3,4,2,1],[1,2,3,4],[0,0,2,3]]
3. Modify your script so the output looks likes:
+-+-+-+-+
|0|2|1|4|
+-+-+-+-+
|3|4|2|1|
+-+-+-+-+
|1|2|3|4|
+-+-+-+-+
|0|0|2|3|
+-+-+-+-+
4. Modify your script so the 0 are replaced by a blank space.
+-+-+-+-+
| |2|1|4|
+-+-+-+-+
|3|4|2|1|
+-+-+-+-+
|1|2|3|4|
+-+-+-+-+
| | |2|3|
+-+-+-+-+
'''

def append (the_list):
    y=[]
    inp = str(input("Enter Numbers: ")).strip()+" "
    tempstr=''
    counter=0
    for x in range(len(inp)):
        if(counter>=4):
            break
        if(inp[x]==' '):
            y.append(int(tempstr))
            tempstr=''
            counter-=-1
        else:
            tempstr+=inp[x]
    the_list.append(y)
    pass

x=[]

for y in range(4):
    append(x)
#print(x)
'''
print( f"""+-+-+-+-+
           |0|2|1|4|
           +-+-+-+-+
           |3|4|2|1|
           +-+-+-+-+
           |3|4|2|1|
           +-+-+-+-+
           |3|4|2|1|
           +-+-+-+-+""" )
           '''
for y in range(4):
    print('+-+-+-+-+')
    tempStr = '|'
    for y2 in range(4):
        tempStr+=str(x[y][y2])+'|'
    print(tempStr)
print('+-+-+-+-+')

print('\n\n\n\n')

for y in range(4):
    print('+-+-+-+-+')
    tempStr = '|'
    for y2 in range(4):
        tempStr+=str(x[y][y2])+'|'
    print(tempStr.replace('0',' '))
print('+-+-+-+-+')