'''
Exercise 3: reinventing the wheel!
For this question we are emulating the method split() from the type str. Write the
algorithm for a function splitText(text:String, delimiters:String) which
returns the list of the words by splitting the string text at each delimiters. The delimiters
themselves are discarded. An example is given below:
>>> sampleText = "As Python's creator, I'd like to say a few words about its origins."
>>> splitText(sampleText, ", '.")
['As', 'Python', 's', 'creator', 'I', 'd', 'like', 'to',
'say', 'a', 'few', 'words', 'about', 'its', 'origins']
You can assume that a string has a method contains(Character) that returns true if the
character is in the string, false otherwise. This exercise is more challenging than it may look
like. 
'''
def split_text(text, seperator):
    temptext = ''
    array = []
    if text=='' or seperator=='':
        return []
    for x in text+seperator[0]:
        if x in seperator:
            if not (temptext == ''):
                array.append(temptext)
                temptext=''
        else:
            temptext+=x
    return array

print(split_text("  As Python's creator, I'd like to say  ", ','))