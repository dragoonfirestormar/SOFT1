'''
Exercise 3: Cryptography, Caesar Cipher
In cryptography, a Caesar cipher, also known as the shift
cipher, is one of the simplest and most widely known
encryption techniques. It is a type of substitution cipher in
which each letter in the plain text is replaced by a letter some
fixed number of positions down the alphabet.
For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The
method is named after Julius Caesar, who used it to communicate with his generals.
Mathematically, a Caesar cipher can be
expressed by the following equation:
c = (p + a) mod 26
Here, ‘mod 26’ means that you use clock
arithmetics for values greater than 26, i.e.,
0=26 mod 26, 1=27 mod 26, 2=28 mod 26,
…, 0=52 mod 26, 1=53 mod 26, …, 10=62
mod 26, and so on.
1. Write a script that encrypts a plain text into a cypher text using the Caesar Cipher
algorithm.
2. Write a script that decrypts a cipher text into a plain text using the Caesar Cipher
algorithm. 
'''
word = str(input("Enter your sentence: ")).lower()

encription=''
n=3
for x in word:
    if x >= 'a' and x <= 'z':
        if x <= chr(ord('z')-n):
            encription += chr(ord(x)+3)
        else:
            encription += chr(ord('a') + ord(x) - (ord('z')-n) -1)
    else:
        encription += x
    
dencription=''
for x in word:
    if x >= 'a' and x <= 'z':
        if x >= chr(ord('a')+n):
            dencription += chr(ord(x)-3)
        else:
            dencription +=  chr(ord('z') - n +ord(x) +1 -ord('a')) 
    else:
        dencription += x

print(encription.upper())
print(dencription.lower())