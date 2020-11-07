'''
Exercise 1:
Write a script to save the content of a string variable a_word into a file called exo1.txt.
'''
a_word = "week5_practical4b_1"

with open('exo1.txt', 'w') as x:
    x.write(a_word)

