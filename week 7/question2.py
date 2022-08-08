from cmath import sqrt

from pyparsing import WordEnd

C = 50
H = 30
def calculate(D):
    return sqrt((2*C*D)/H)
# d = 

word = "hello world and practice makes perfect and hello world again".split()
for i in word:
    if word.count(i)>1:
        word.remove(i)
word.sort()
# print(" ".join(word))

word = "hello world and practice makes perfect and hello world again".split()
[word.remove(i) for i in word if word.count(i)> 1]
word.sort()
# print(" ".join(word))

s = "Hello World"
d = {
    "UPPERCASE": 0,
    "LOWERCASE": 0
}
for c in s:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
      pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])
