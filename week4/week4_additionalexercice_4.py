'''
Exercise 4: extension of exercise 3 Practical 2
In cryptography, a Caesar cipher, also known as the shift cipher, is one of the simplest and
most widely known encryption techniques. It is a type of substitution cipher in which each
letter in the plain text is replaced by a letter some fixed number of positions down the alphabet.
For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The
method is named after Julius Caesar, who used it to communicate with his generals.
Mathematically, a Caesar cipher can be expressed by
the following equation:
c = (p + a) mod 26
Here, ‘mod 26’ means that you use clock arithmetic for
values greater than 26, i.e., 0=26 mod 26, 1=27 mod
26, 2=28 mod 26, …, 0=52 mod 26, 1=53 mod 26, …,
10=62 mod 26, and so on.
1. Write a function caesar_encrypt that encrypts a plain text into a cypher text using
the Caesar Cipher algorithm. What parameters are needed? Should the function return
something? For simplicity, assume that only alphabet letters are encrypted, other
symbols remain the same.
2. Write a function caesar_decrypt that decrypts a cipher text into a plain text using
the Caesar Cipher algorithm. What parameters are needed?
3. Given the cipher text below, and knowing it has been encrypted using a Caesar Cipher
algorithm, could you decrypt it?
"bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
bmtt bpmu bw lw.”
'''
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

string = """bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc
bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc
bmtt bpmu bw lw."""

for _ in range(32-12):
    string = caesar_decrypt(string)

print(string)