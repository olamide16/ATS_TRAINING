from re import A


def fibo(n):
    a = 0
    b = 1
    for i in range(0,n):
        temp = a
        a = b
        b += temp
    return(a)
for c in range(0, 100):
    print(fibo(c)) 