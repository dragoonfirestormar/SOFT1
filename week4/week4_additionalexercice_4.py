def caesar_encrypt(text):
    encription=''
    n=3
    for x in text:
        if x >= 'a' and x <= 'z':
            if x <= chr(ord('z')-n):
                encription += chr(ord(x)+3)
            else:
                encription += chr(ord('a') + ord(x) - (ord('z')-n) -1)
        else:
            encription += x
    return encription

def caesar_decrypt(text):
    dencription=''
    n=3
    for x in text:
        if x >= 'a' and x <= 'z':
            if x >= chr(ord('a')+n):
                dencription += chr(ord(x)-3)
            else:
                dencription +=  chr(ord('z') - n +ord(x) +1 -ord('a')) 
        else:
            dencription += x
    return dencription

print(caesar_decrypt("""bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
bmtt bpmu bw lw."""))