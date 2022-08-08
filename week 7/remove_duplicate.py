li = [1,2,2,3,4,5,5,72,9]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)