def display_dico(dico):
    for x in dico:
        print(f"{x} --> {dico[x]}")

x = {'un':1, 'deux':2, 'trois':3}
display_dico(x)