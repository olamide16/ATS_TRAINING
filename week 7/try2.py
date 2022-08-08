# expression = input("Enter an expression: ")
# print(eval(expression))

import random
from random import shuffle

# print( random.choice([i for i in range(11) if i % 2 == 0]))
# print (random.choice([i for i in range (10,151) if i % 5 ==0 and i % 7 == 0]))
# print(random.sample(range(100,201)))
li = [3,6,7,8]
shuffle(li)
# print(li)


subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print (sentence)