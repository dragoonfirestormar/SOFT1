'''
Exercise 1:
In Python, to compute the sum of all elements in a list, you can use the built-in function sum.
For example:
>>> sum([1,2,3,4])
10
>>> sum([])
0
However, sum does not work with multidimensional lists (see example below):
>>> sum([1,[2,3],4])
Traceback (most recent call last):
 File "<pyshell#5>", line 1, in <module>
 sum([1,[2,3],4])
TypeError: unsupported operand type(s) for +: 'int' and
'list'
Write a recursive algorithm (using pseudo-code) sum_all(numbers:list):list that
takes a multidimensional list of integers as parameters and returns the sum of all elements in
that list. Note, empty lists sum to 0. For examples:
>>> sum_all([1,[2,3],4])
10
>>> sum_all([1,[2,[3,[4]]]])
10
>>> sum_all([1,2,3,4])
10
>>> sum_all([1,[]])
1
'''
def sum_all(numbers):
    if numbers == []:
        return 0
    if type(numbers[0]) is list:
        return sum_all(numbers[0]) + sum_all(numbers[1:])
    else:
        return numbers[0] + sum_all(numbers[1:])


print(sum_all([1,[2,[3,[4]]]]))