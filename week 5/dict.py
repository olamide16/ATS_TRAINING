import random
num_dict = []
for i in range(1,20):
    num = random.randint(1,99)
    num_dict.append(num)
for i in num_dict:
    if i not in num_dict:
        print(num_dict)
    else:
        pass
print(num_dict)

