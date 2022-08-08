li = [x for x in range(1,201) if x %2 != 0]
li_range2 = [10,23,45,67]
li_range = [1,2,3,4,5,6,7,8]
li2 = [x for x in range(1,201) if x % 5 != 0 and x % 7 != 0]
li3 = [x for (i,x) in enumerate(li_range) if i % 2 != 0 and i <=6]
li4 = [x for (i,x) in enumerate(li_range) if i <3 or 4< i]
li5 = [x for (i,x) in enumerate(li_range) if i not in (0,4,5)]
li6 = [x for (i,x) in enumerate(li_range) if x != 8]
set1 = set(li_range)
set2 = set(li_range2)
intersection = set1 & set2
li_rev = li_range[:: -1]
print(li_rev)