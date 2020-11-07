'''
Exercise 6:
We want to create a function sum_from_file(filename) that calculate the sum of all
int contained in the text file filename. The format of the text file is as follow, a series of
int separated by a space spanning several lines as shown below. In this particular case, the
returned value should be 100.
1 30 4 5
8 12 19 1
5 5 10
1. Should the function raise an error? If yes, describe the case(s) where an error should be
raised.
2. It is sometime useful to decompose the problem into smaller problem. In this case it
would be useful to have a function sum_numbers(a_string) that calculates and
returns the sum of all numbers contained in the string a_string. The format of the
string is a series of int separated by a space. For example:
>>> sum_numbers('1 30 4 5')
40
Note: It could be useful to remember /check some the methods already existing for str
object.
3. Now that we have managed to write sum_numbers, it should be easier to write the
function sum_from_file.
4. Write the docstring (python documentation) for this function, as explain in chapter 7 of
the textbook. 
'''
def sum_from_file(filename):
    with open('exo1.txt') as x:
        temp=''
        su=0
        for y in x.read()+' ':
            if(y==' ' or y=='\n'):
                su+=int(temp)
                temp=''
                pass
            else:
                temp+=y
        return su

print(sum_from_file('exo1.txt'))