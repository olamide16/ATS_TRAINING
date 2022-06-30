def vowel(c):
    newstr = []
    vowel = ('a','e','i','o','u')
    for x in c.lower():
        if x in vowel:
            newstr = newstr.replace(x,"")
    return newstr
print(vowel)