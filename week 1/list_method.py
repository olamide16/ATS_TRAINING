import numbers


num = [5,2,1,7,4]
num.append(20)
num.insert(0,10)
num.remove(5)
# num.clear()
num.pop()
print(num.index(1))
print(7 in num)
print(num.count(2))
num.sort()
num.reverse()
num2=num.copy()
num.append(10)
print(num2)
# print(num)