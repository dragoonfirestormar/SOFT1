'''
Exercise 2: from a resit paper.
You must use the file textanalysis.py to answer this question. Write a function
get_words_starting_with(text, letter) that returns the list of words starting
with letter in the string text. The result should not be case sensitive, e.g. ’about’ should
be returned if the letter ’a’ or ’A’ is given as parameter. For simplicity, we assume for exercises
2,3, and 4 that the text does not have any punctuations, and words are separated by at least one
blank space.
For example, using the variable sample_text we should obtain:
>>> get_words_starting_with (sample_text, ’a’)
[’As’, ’a’, ’about’, ’adding’, ’a’, ’ago’, ’a’,
’around’, ’Amsterdam’, ’a’, ’and’, ’an’, ’about’,
’a’, ’ABC’, ’appeal’, ’as’, ’a’, ’a’, ’a’]
>>> get_words_starting_with(sample_text, ’z’)
[]
Hint: You may want to use the method split() from the str type.
Exercise 3: from a resit paper.
As you can see in question 2, there are many repetitions of the word ’a’ in the list. Improve
your solution so no repetition of the same word occurs in the list.
>>> get_words_starting_with(sample_text, ’a’)
[’As’, ’a’, ’about’, ’adding’, ’ago’, ’around’,
’Amsterdam’, ’and’, ’an’, ’ABC’, ’appeal’, ’as’]
'''
def get_words_starting_with(text, letter):
    counter=''
    result=[]
    NoRepeatedResult=set()
    for x in  (text.strip()+' '):
        if(x==' '):
            if(counter[0].lower()==letter.lower()):
                result.append(counter)
                NoRepeatedResult.add(counter)
            counter=''
        else:
            counter+=x
    return (result, NoRepeatedResult)

print(get_words_starting_with(input('Enter Your Sentence: '),input('Enter the alphabet: ')))