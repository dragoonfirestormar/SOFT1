def save_list2file(sentences, filename):
    with open(filename,'w') as x:
        for y in sentences:
            print(y, file=x)

save_list2file(['yikes','lolxd'],'ayy')