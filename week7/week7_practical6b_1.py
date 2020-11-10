'''
Exercise 1:
We are now able to compare two vectors, however it would be nice if we could use the operator
== instead of .equals(…). Fortunately Python allows to overload operators such as +, *,
== and !=. To overload the operator ==, we must override the method __eq__. (for the
operator !=, override the method __ne__).
Implement the two methods:
def __eq__(self, other_vector):
 <body>
def __ne__(self, other_vector):
 <body>
'''

#Complete Answer Is Within Vector.py


def __eq__(self, matrix):
        return self.equal(matrix)
    
def __ne__(self, matrix):
        return not(self.equal(matrix))