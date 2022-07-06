import random

list_num = []
list_keys = []
for i in range(0,99):
    x = random.randint(1,99)
    list_num.append(x)
    if len(list_num) == 20:
        break
# print(list_num)
list_key = [str(j) for j in  list_num]
# print(list_key)
num_dict = dict(zip(list_key,list_num))
print(num_dict)