'''
Exercise 2:
1. Write a script that takes a sentence from the user without any punctuation and prints
the sentence without any white spaces. Note a white space is represented by ' ', and
an empty string is represented by ''.
>>> enter a sentence: this is a SHORT sentence
thisisaSHORTsentence
2. Same as above except that each word in the output should start with a upper case letter
and all other letter should be lower case (also known as CamelCase).
>>> enter a sentence: this is a SHORT sentence
ThisIsAShortSentence
3. Write a script that takes a sentence from a user written in CamelCase (without any blank
spaces), creates the list of words from that sentence, and then prints that list.
>>> enter a sentence in CamelCase: ThisIsAShortSentence
['This','Is','A','Short','Sentence']
'''

word = str(input("Enter Your Sentence: "))
words = word.lower()
print(word.replace(" ",""))

wordWOspace = ""
wordCamelCase = ""
tempString = ""
camelList = []
for x in range(0, int(len(word))): 
    if word[x] != " ":
        wordWOspace+=word[x]
    
    if x == 0:
        wordCamelCase += words[x].upper()
    elif word[x-1] == " ":
        pass
    elif word[x] == " ":
        wordCamelCase += words[x+1].upper()
    else:
        wordCamelCase+=words[x]

    if word[x] >= 'A' and word[x] <='Z' and x>0:
        camelList.append(tempString)
        tempString=word[x]
    else: 
       tempString+=word[x]

camelList.append(tempString)
print(wordWOspace)
print(wordCamelCase)
print (camelList)
