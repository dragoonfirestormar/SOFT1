'''
Exercise 3:
There is a way to add the following functionality to our class Vector.
>>> vector1 = Vector(1, 2, 3, 5, 6, 1)
>>> vector1[2] += 5
>>> print(vector1)
<1.0, 2.0, 8.0, 5.0, 6.0, 1.0>
Search the web to find out how it can be done (I will NOT provide the answer). For method
with undefined number of parameters search *args. Note, the tests provided in previous
practical should still be working, including the test for the __init__ method.
'''

#Complete Answer Is Within Vector.py

def __getitem__(self, position):
        return self.getValue(position)

def __setitem__(self, position, value):
        return self.setValue(position, value)