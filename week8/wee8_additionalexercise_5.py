'''
def game(index, sequence):
    if index - 1 > 0:
        return [sequence[0]] + game(index-1, (sequence[1], sequence[0]))
    else:
        return [sequence[0]]
'''

def reci(arr, num=None):
    if arr[0]==arr[-1]:
        arr.append(arr[1])
    else:
        arr.append(arr[0])
    return arr

def game(index, sequence):
    if index > 0:
        if index-4>=0:
            return game(index-1, reci(sequence,1)) + ' '+ game(index-2, reci(sequence,2)) + ' '+ game(index-4, reci(sequence,3))
        elif index-2>=0:
            return game(index-1, reci(sequence,1)) + ' '+ game(index-2, reci(sequence,2))
        elif index-1>=0:
            return game(index-1, reci(sequence,1))
    else:
        return ''.join(sequence[2:])



print( game(4, ['a', 'b']) )