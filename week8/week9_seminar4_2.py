'''
Exercise 2: wildcard pattern
Given a binary pattern that contains ‘?’ wildcard character at few positions, find all possible
combinations of binary strings that can be formed by replacing the wildcard character by either
0 or 1. For example, for wildcard pattern 1?11?00?1?, the possible combinations are
1011000010 1011000011 1011000110 1011000111
1011100010 1011100011 1011100110 1011100111
1111000010 1111000011 1111000110 1111000111
1111100010 1111100011 1111100110 1111100111
We can easily solve this problem using recursion. The idea is to process each character of the
pattern one by one and recur for the remaining pattern. If the current digit is 0 or 1, we ignore
it and if the current character is a wildcard character ‘?’, we replace it with 0 & 1 and recur
for the remaining pattern. You may need a convenience function with a parameter that keep
track of the partial solution you built so far, and another parameter storing all the previous
solutions you found
'''
def wildcard(string):
    if not '?' in string:
        return [string]
    else:
        return wildcard(string.replace('?','1',1))  + wildcard(string.replace('?','0',1))

print(wildcard('1?11?00?1?'))

