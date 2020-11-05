def concatDico(dico1, dico2):
    ayy = {}
    for k,v in dico1.items():
        ayy[k]=v
    for k,v in dico2.items():
        ayy[k]=v

    print (ayy)

concatDico({'“one”':1, '“two”':2, '“three”':3}, {'“four”':4, '“five”':5})


def concatDico2(dico1, dico2):
    ayy = {}
    for k,v in dico1.items():
        if k in dico2:
            ayy[k]=[v,dico2[k]]
            del dico2[k]
        else:
            ayy[k]=v
    for k,v in dico2.items():
        ayy[k]=v

    print (ayy)

concatDico2({'“one”':1, '“two”':2, '“five”':5},{'“two”': '”10”', '“five”':'”101”'})
