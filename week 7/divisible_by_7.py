list= []
for i in range (2000, 3200):
    if  (i % 7 == 0 and i % 5 != 0):
        list.append(i)
# print(list)

# OR
list = [i for i in range (2000,3201) if i % 7 == 0 and 1 % 5 != 0]
# print(list)

fact = 1
# num = int(input("Enter a number: "))
# for i in range (1, num +1):
    # fact = fact * i
# print(fact)

num = int(input("Enter a value: "))
d = dict()
for i in range (1, num+1):
    d[i] = i * i
print (d)
    