my_list = [num for num in "1234567"]
odd_num = [num**(1/2) for num  in range(1,10)]
even_num = [num for num  in range(1,10) if num % 2 == 0]
# set comprehension and list comprehension are ahe same
print(even_num)
#dict comprehension
simple_dict = {
    "a" : 1,
    "b" : 2
}
# my_dict = {key: value ** 2 for  key,value in simple_dict.items()if value % 2 == 0}
# my_dict = {num: num *2 for num in [1,2,3]}
# print(my_dict)