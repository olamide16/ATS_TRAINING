fibo_num = int(input("Enter a num: "))
fib_start = 0
series = 1
if fibo_num < 0:
    print(0)
else:
    print(fib_start)
    print(series)
    for x in range(2, fibo_num):
        fib =fib_start + series
        print(fib)
        fib_start = series
        series = fib