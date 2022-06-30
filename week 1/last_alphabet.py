from os import remove


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
first_ten = alphabet[0:9]
vowel = ['a','e','i','o','u']
consonant = alphabet.remove(vowel)

    
print(consonant)
print(vowel)
print(first_ten)
last_ten = alphabet[-10:-1]
print(last_ten)
