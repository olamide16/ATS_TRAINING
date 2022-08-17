def factor(n):
    factors = []
    for i in range(1,n +1):
        if n % i == 0:
            factors.append(i)
    print(factors)

# factor(n = int(input("Enter a number: ")))

def factorial(n):
    j = 1
    for i in range(1,n+1):
        j = j * i
    return(j)
# print(factorial(n = int(input("Enter a number: "))))

def prime_num(n):
    prime = []
    j = 0
    for i in range(1 , n+1):
        if (n%i == 0):
            j = j +1
            prime.append(i)
        return(j)
# print(prime_num(n = int(input("Enter a number: "))))

def prime(n):
    prime_list= []
    for i in range (1, n +1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime_list.append(i)
    print(prime_list)
# prime(n = int(input("Enter a number: ")))

def tables_Multip(n):
    for i in range(1,13):
        print(n, "x", i, "=", i * n)
# tables_Multip(n= int(input("Enter a number: ")))

def all_tables_Multip(n):
    for i in range (1,n+ 1):
        print("\nThe Multiplication of table", i)
        for j in range(1, 13):
            print(i, "x", j, "=", i * j)
# all_tables_Multip(n= int(input("Enter a number: ")))


def palidrome(n):
    # if len(n) > 1:
        number = n
        rev = 0
        while(n > 0):
            dig = n % 10
            rev = rev * 10 + dig
            n = n//10
            # print(rev)
        if number == rev:
            print("Palindrome")
        else:
            print("Not a palindrome")
# palidrome(n=int(input("Enter a palindrome number: ")))

def num_pali(n):
    if n == n[::-1]:
        # print(n)
        print("Palindrome")
    else:
        print("Not a palindrome")
# num_pali(n=(input("Enter a palindrome number: ")))

def fibo(n):
    fibo_series = [0,1]
    a =0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        # print(0)
        fibo_series.append(0)
    elif n == 1:
        # print(b)
        fibo_series.append(1)
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
            fibo_series.append(b)
    # print(fibo_series)
        print(b)
            # print(b)
# fibo(n=int(input("Enter a number: ")))


def cube_num(n):
    for i in range(1,n+1):
        if n > 0:
            print(f"Current Number is: {i} and the cube is {i ** 3}")
        else:
            print(0)
# cube_num(n=int(input("Enter a number: ")))


