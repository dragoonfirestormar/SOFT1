'''
Exercise 1: reinventing the wheel! (From Seminar 1 exercise 3)
For this question we are emulating the method split() from the type str. This exercise is
more challenging than it may look like. It is crucial that you devise an algorithm before you
start implementing. Implement your own pseudo-code or the one given in the model answers.
There are methods in the str type that can help you identify between an alphabet character
and a punctuation; this might be very useful.
Using the file practical_5.py, write a function split_text(text, separators)
where text is a string to be split, separators is a string containing all the characters used
to split the text (for example ‘,.!? ’). The function returns the list of tokens separated by
one of the separators. For example:
>>> sample_text = "As Python's creator, I'd like to say a
few words about its origins.”
>>> split_text(sample_text, “,’.”) #no space delimiter
['As Python', 's creator', ' I',
'd like to say a few words about its origins']
>>> split_text (sampleText, ", '.") [
'As', 'Python', 's', 'creator', 'I', 'd', 'like', 'to',
'say', 'a', 'few', 'words', 'about', 'its', 'origins']
You must NOT use the method split() from the str type, however other methods from
the class are allowed. You must not use python libraries such as string.py. 
'''
def split_text(text, separators):
    temp=''
    words=[]
    for x in text:
        temp+=x
        for y in separators:
            if x==y:
                words.append(temp[:-1])
                temp=''
                break
    return words

print(split_text("As Python's creator, I'd like to say a few words about its origins.", '\',.'))

            
