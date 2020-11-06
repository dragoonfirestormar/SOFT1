import string
def get_words_frequencies(text):
    freq = {}
    temp = ''
    for x in text.lower()+' ':
        if not (x in string.punctuation or  x==' '):
            temp+=x
        else:
            if temp in freq:
                freq[temp]+=1
            else:
                freq[temp]=1
            temp=''
    return freq

print(get_words_frequencies("As Python's creator, I'd like to say a few words about its origins."))