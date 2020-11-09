'''
Exercise 6:
In Programming, being able to compare objects is important, in particular determining if two
objects are equal or not. Let’s try a comparison of two vectors:
>>> vector1 = Vector([1, 2, 3])
>>> vector2 = Vector([1, 2, 3])
>>> vector1 == vector2
False
>>> vector1 != vector2
True
>>> vector3 = vector1
>>> vector3 == vector1
True
As you can see, in the current state of implementation of our class Vector does not produce the
expected result when comparing two vectors. In the example above the == operator return
True if the two vectors are physically stored at the same memory address, it does not compare
the content of the two vectors.
Therefore, you need to implement a method equals(other_vector) that returns True
if the vectors are equals (i.e. have the same value at the same position), False otherwise.
'''

#Complete Answer Is Within Vector.py

def equal(self, matrix):
        if not(isinstance(matrix,Vector)):
            return 'TypeError'
        if self._vector==matrix._vector:
            return True
        else:
            return False