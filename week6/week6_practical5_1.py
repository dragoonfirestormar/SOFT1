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

            
