'''
Exercise 2:
In exercise 1, there could be many repetitions of the same word in the returned list. Rather than
just returning the duplicated words, perhaps it would be more interesting to keep track of the
number of occurrences of each word. For example, in the variable sample_text given in
the file practical_5.py, ‘a’ occurs 9 times, while ‘as’ occurs twice (one ‘As’ and one ‘as)
and ‘python’ three times.
Using the file practical_5.py implement get_words_frequencies(text)which
returns the result of our computation, that is for each word in text, provide its number of
occurrences in text. The function should be case insensitive, meaning that ‘As’ and ‘as’
should be considered the same. The method returns a dictionary where the keys are the words
in lowercase and the values are the frequency of the given word in the text passed in
parameters.
Note the module string contains a variable punctuation which is a string containing
all punctuation symbols but does not contain the white space.
'''
import string
def get_words_frequencies(text):
    freq = {}
    temp = ''
    for x in text.lower().strip()+' ':
        if not (x in string.punctuation or  x==' '):
            temp+=x
        else:
            if temp == '':
                pass
            elif temp in freq:
                freq[temp]+=1
            else:
                freq[temp]=1
            temp=''
    return freq 

print(get_words_frequencies(". to Be, or Not TO be! "))