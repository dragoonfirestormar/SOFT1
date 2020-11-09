'''
Exercise 2:
Another very useful method to write is __str__. This will enable us to print the content of
the instance using the print function. For the purpose of this exercise we have decided to
represent the vector [
𝑎
𝑏
𝑐
] with the string '<a, b, c>' to differentiate it from a list.
Implement __str__.
 def __str__(self):
 pass
Lilian Blot Software 1
P a g e | 2
Now let see how we can instantiate (create) some vectors.
>>> my_vector = Vector([1, 2, 3])
>>> print(my_vector)
<1, 2, 3>
>>> empty_vector = Vector()
>>> print(empty_vector)

'''

#Complete Answer Is Within Vector.py

def __str__(self):
        add=''
        if self._vector == None:
            add=''
            pass
        else:
            for x in range(len(self._vector)):
                add +=  (str(self._vector[x]) + ', ')
                pass
        return '<'+add[:-2]+'>'