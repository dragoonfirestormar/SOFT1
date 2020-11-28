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

# Single line approch for Palindrome but takes longer time, as its revereses the string
print( ('yes' if word[::-1]==word else 'no') )

#This approch goes from both ways, left and right and sees if the frist and last indez are both same
#If not then word can not be palindrome and it will give result faster
counter = True
for x in range(int(len(word))):
    if word[x]!=word[-x-1]:
        counter=False
        break
    pass

if(counter):
    print("YES!")
else:
    print("NO!")

#This is to get only words out of sentences.
updatedword = ""
for x in word:
    if x>='a' and x <='z':
        updatedword += x

print( ('yes' if updatedword[::-1]==updatedword else 'no') )

##################################################################

#This method is easiest plus it will ignore all the cases where its not an english alphabet

counter = True
print(word)
x = 0
y = 0
while(x<=int(len(word)/2)):
    if not( word[x] >='a' and word[x] <='z' ):
        x+=1
        continue
    if not( word[-y-1] >='a' and word[-y-1] <='z' ):
        y+=1
        continue
    #if x >= int(len(word))
    if word[x]!=word[-y-1]:
        counter=False
        break
    x+=1
    y+=1
    pass

if(counter):
    print("YES!")
else:
    print("NO!")