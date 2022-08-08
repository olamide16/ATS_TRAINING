def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 1/2)
    return result
my_list = make_list(10)
print(my_list)