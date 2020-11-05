def reverse_dictionary(dico):
    ayy={}
    for k in dico:
        if dico[k] in  ayy:
            print("Error")
            return None
        ayy[dico[k]]=k
    print(ayy)

reverse_dictionary({'“one”':1, '“two”':2})