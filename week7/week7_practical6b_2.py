'''
Exercise 2:
Instead of using the method add(…) and scalar_product(…) we would like to overload
the operators + and *. The vector addition operator is commutative, i.e. v1+v2 == v2+v1
and we can override the method __add__ to overload the + operator. When considering the
multiplication, it is a little bit more complicated, 3 * v1 is allowed, but v1 * 3 is not.
Investigate the methods __mul__ and __rmul__. One other programming shortcut we
could find useful is v1 += v2 for v1 = v1+v2. It can be implemented by overloading
__iadd__. Similarly, the shortcut v1 *= 3 for v1 = 3 * v1 can be implemented by
overloading __imul__. Implement all these operators overloading.
'''

#Complete Answer Is Within Vector.py

    def __add__(self, matrix):
        return self.addition(matrix)

    def __mul__(self, intValue):
        return self.scalar(intValue)
 
    def __rmul__(self, intValue):
        return self.scalar(intValue)

    def __iadd__(self, matrix):
        return self.addition(matrix)
    
    def __imul__(self, intValue):
        return self.scalar(intValue)