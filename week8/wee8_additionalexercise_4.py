t9_keypad = {'2':['a','b','c'], '3':['d','e','f'],
            '4':['g','h','i'], '5':['j','k','l'],
            '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z']}

def prediction(number, keypad):
    if len(number) == 0:
        return []
    if len(number) == 1:
        temp=[]
        for x in keypad[number]:
            temp+=x
        return temp
    else:
        temp=[]
        for x in keypad[number[0]]:
            temp+=x
        toAdd = prediction(number[1:], keypad)
        Og = []
        for x in temp:
            for y in toAdd:
                Og.append(x+y)
        return Og

print(prediction('78634',t9_keypad))