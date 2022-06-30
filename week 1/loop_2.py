import numbers


numbers = [2, 2, 2, 2, 7]
for x in numbers:
    # print('x' * x)
    output = ""
    for count in range(x):
        output += 'x'
    print(output)