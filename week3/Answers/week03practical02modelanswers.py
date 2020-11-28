######################### EXERCISE 1 #########################################
# A common error is to reverse the word and compare if it is equal to itself.
# This is an ineficient implementation, it is better to use two pointers
# (indices) moving from both ends and compare if they point to the same 
# character.

sentence = input('Enter a sentence: ')
sentence = sentence.lower()
front_index = 0
# remember that the index of the last element of a string is the lenght of the
# string minus 1 (as the indexing starts at 0).
rear_index = len(sentence) - 1 

# We assume the sentence to be a palindrom and try to see if is right or not
# It is quite common tp make an assumption and try to disprove it. If we can't
# disprove it, the assumption is true.
is_palindrom = True

while is_palindrom and front_index < rear_index: 
    # A note about style, it is preferred to write is_palinfrom rather than
    # is_palindrom == True.
    if sentence[front_index] != sentence[rear_index]:
        is_palindrom = False
    front_index += 1
    rear_index -= 1

if is_palindrom:
    print('It is a palindrom.')
else:
    print('it is NOT a palindrom')
    

# Hint for the advanced bit: you may want to move the two pointers 
# independently 



######################### EXERCISE 2 #########################################

#######################    part 1    #########################################
sentence = input('Enter a sentence: ')
output = ''
for letter in sentence:
    if letter != ' ':
        output += letter

print(output)




#######################    part 2    #########################################
sentence = input('Enter a sentence: ')
output = ''

# We need to set up a FLAG that tells us if the next character is the first
# Character of the next word. We can use a boolean variable, let's call it
# first_letter. We need to assign the value True as the next character will
# be the first of the sentence and therefore the first of a word.
first_letter = True

for letter in sentence:
    if letter != ' ':
        if first_letter:
            # The character is the first of a word so must be
            # upper case
            output += letter.upper()
            first_letter = False
        else:
            output += letter.lower()
    else: #means that the next character will be the first one of a new word
        first_letter = True

print(output)




#######################    part 3    #########################################
sentence = input('Enter a sentence: ')
output = ''

# We need to set up a FLAG that tells us if the next character is the first
# Character of the next word. We can use a boolean variable, let's call it
# first_letter. We need to assign the value True as the next character will
# be the first of the sentence and therefore the first of a word.
first_letter = True

# We also need an ACCUMULATOR to store the content of the current word we
# are buiding. We initialise the accumulator to an empty string ''.
current_word = ''

# Finally we need another ACCUMULATOR to build the list of word. It is
# initialised to an empty list [].
output = []

for letter in sentence:
    if letter.isupper():
        if current_word != '':  # This is the start of a new word, and 
                                # therefore current_word is completed
                                # and should be added to output.
            output.append(current_word)
        current_word = letter # we just started a new word
    else: 
        current_word += letter

# We must be careful, when we finished to go through the sentence, we did not
# add the last word.
output.append(current_word)
print(output)


######################### EXERCISE 3 #########################################

#########################   part 1   #########################################

plaintext = input("Enter message to encrypt: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3
cypher_text = ""
for letter in plaintext:
    if letter in alphabet:
        index = alphabet.index(letter)
        substitution_index = (index + shift) % len(alphabet)
        cypher_text = cypher_text + alphabet[substitution_index]
    else:
        cypher_text = cypher_text + letter

print(cypher_text)

#########################   part 2   #########################################

# Will decipher the encrypted text from previous question, I should retrieve 
# the original plain text.
plaintext = ""
for letter in cypher_text:
    if letter in alphabet:
        index = alphabet.index(letter)
        substitution_index = (index - shift) % len(alphabet)
        plaintext = plaintext + alphabet[substitution_index]
    else:
        plaintext = plaintext + letter

print(plaintext)
