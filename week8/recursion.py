'''
Exercise 1:
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a recursive
function called is_power(a,b) that takes parameters a and b and returns True if a is a
power of b, False otherwise.
For example:
• 27 is power of 3 if 27/3 = 9 is power of 3, that is 9/3 = 3 is power of 3, which is true.
• 18 is power of 3 if 18/3 = 6 is power of 3, that is if 6/3 = 2 is power of 3 which is false.
Could you also write an iterative version of this function?
Exercise 2:
To compute the sum of all elements in a list, you can use the built-in function sum.
For example:
>>> sum([1,2,3,4])
10
>>> sum([])
0
Write a recursive function rec_sum(numbers) that take a list of integers as a parameter
and returns the sum of all the elements in the list. The function should return 0 if the list is
empty.
Lilian Blot Software 1
P a g e | 5
Exercise 3: (from practical 03)
During practical 03, we implemented the function sum_digits(number) to calculate and
return the sum of digits of a given whole number (int) given as parameter. For example,
>>> print(sum_digits(1234))
10
At the time we used loops in our implementation. This time you must use recursion. In
addition, you are not allowed to convert the int into a list or a string.
Exercise 4:
Write a recursive function flatten(mlist) where mlist is a multidimensional list that
returns all the element from mlist into a one-dimensional list. Note, empty lists are ignored.
For examples:
>>> flatten([1,[2,3],4])
[1,2,3,4]
>>> flatten([1,[2,[3,[4]]]])
[1,2,3,4]
>>> flatten([1,2,3,4])
[1,2,3,4]
>>> flatten([1,[]])
[1]
Exercise 5: (from seminar 1)
Write a recursive function merge(sorted_listA, sorted_listB) that merges the
two lists into a single sorted list and returns it. The two parameters are list of comparable
objects that are sorted in ascending order. For example, the lists contain only strings, or the
lists contain only numbers. Neither of the two lists in the parameters must be modified.
Exercise 6: An unexpected coding journey
A word is considered elfish if it contains all the letters: e, l, and f in it, in any order. For
example, we would say that the following words are elfish: whiteleaf, tasteful, unfriendly, and
waffles, because they each contain those letters.
a) Write a predicate function called iselfish(word) that, given a word, tells us if that
word is elfish or not. The function must be recursive.
b) Write something_ish(pattern, word)a more generalized predicate function
that, given two words, returns true if all the letters of pattern are contained in word.
I did not provide a unit test for this exercise, if you wish you could try to create a unit test for
that exercise and share it with someone else to test their code. 
'''
def is_power(a,b):
    if a==b:
        return True
    if b==0 or b==1:
        return False
    if a==1:
        return True
    if a<b:
        return False
    if a/b == b:
        return True
    else:
        return is_power(a/b,b)


def rec_sum(numbers):
    if len(numbers) == 0:
        return 0 
    else:
        return numbers[0] + rec_sum(numbers[1:])

def sum_digits(number):
    if number <0:
        number*=-1
    if number<9:
        return number
    else:
        temp = (int) (number/10)
        return (number-temp*10) + sum_digits(temp)



def flatten(mlist):
    if(len(mlist)<1):
        return []
    if type(mlist[0]) is list:
        return flatten(mlist[0]) + flatten(mlist[1:])
    else:
        return [mlist[0]] + flatten(mlist[1:])


def merge(sorted_listA, sorted_listB):
    if sorted_listA == [] and sorted_listB == []:
        return []
    if sorted_listA == []:
        return sorted_listB
    if sorted_listB == []:
        return sorted_listA
    if sorted_listA[0]<=sorted_listB[0]:
        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
    else:
        return [sorted_listB[0]] + merge(sorted_listA, sorted_listB[1:])

def iselfish(word, pattern='elf'):
    if len(pattern) < 1:
        return True
    if pattern[0] in word:
        return True and something_ish(pattern[1:], word)
    else:
        return False

def something_ish(pattern, word):
    if len(pattern) < 1:
        return True
    if pattern[0] in word:
        return True and something_ish(pattern[1:], word)
    else:
        return False
#print(iselfish('whiteleaf'))
