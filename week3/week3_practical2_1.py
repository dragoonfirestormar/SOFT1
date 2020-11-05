'''
A palindrome is a word, phrase, number, or other sequence of units that may be read the same
way in either direction, ‘radar’ and ‘Delia saw I was ailed’ are palindromes,
whereas ‘reader’ is not. Write a program that take a sentence or a word as an input and
print if it is a palindrome or not.

The advanced bit
‘Dammit, I'm mad!’ is also considered a palindrome when neither punctuation nor
spaces are taken into account. Change your program so it can recognise these palindromes too.
'''

word = input("Enter the Sentance: ").lower()
print( ('yes' if word[::-1]==word else 'no') )

counter =0
for x in range(int(len(word))):
    if word[x]!=word[-x-1]:
        print("NO!")
        counter=1
        break
    pass

if(counter==0):
    print("YES!")

updatedword = ""
for x in word:
    if x>='a' and x <='z':
        updatedword += x

print(updatedword)
print( ('yes' if updatedword[::-1]==updatedword else 'no') )