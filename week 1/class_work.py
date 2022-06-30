import string
from unicodedata import digit
def encode(data:str):
    digits=string.digits
    schars=string.punctuation
    alpha_lower=string.ascii_lowercase
    alpha_uppercase=string.ascii_uppercase
    rev_alpha_lower=alpha_lower[::-1]
    vowels=['a','e','i','o','u']
    vowels_map=['#','$','%','&','*']
    enc=list()
    
    for s in data:
        if s.lower in vowels:
            enc.append(vowels_map[vowels.index(s)])
        elif s in schars:
            enc.append('|'+s)
        elif s in alpha_lower + alpha_uppercase:
            enc.append(s.swapcase())
        elif s in digits:
            enc.append(rev_alpha_lower[digits.index(s)])
    return(''.join(enc))
            
input = input('enter digits')
print()
def decode(data:str):
    digits=string.digits
    schars=string.punctuation
    alpha_lower=string.ascii_lowercase
    alpha_uppercase=string.ascii_uppercase
    rev_alpha_lower=alpha_lower[::-1]
    vowels=['a','e','i','o','u']
    vowels_map=['#','$','%','&','*']
    dec=list()
    for s in data:
        if s.lower() in vowels_map:
            dec.append(vowels[vowels_map.index])
        elif s in schars:
            dec.append('|'+s)
        elif s in alpha_lower + alpha_uppercase:
            dec.append(s.swapcase())
        elif s in digits:
            dec.append('^'+rev_alpha_lower[digits.index(s)])