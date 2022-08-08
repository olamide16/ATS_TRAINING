my_list =[5,4,3]
square_root_list = [81, 9, 169]
new_list = list(map(lambda item: item ** 2, my_list))
list = list(map(lambda num: num ** (1/2), square_root_list))
a = [(0,2),(4,3), (10,-1), (9,9)]
a.sort(key = lambda x: x[1])
print(a)