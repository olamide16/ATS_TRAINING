def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
numbers = int(input("Enter a number: "))
fib_list = []
for x in fib(numbers):
    fib_list.append(x)
print(fib_list)