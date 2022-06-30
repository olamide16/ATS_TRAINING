from enum import unique


num = [1,2,2,3,4,5,6,6,7,8,9, 10,18,17,14,20,12]
unique = []
for number in num:
    if number not in unique:
        unique.append(number)
print(unique) 
