#------Palindrome-------
# num = int(input("Enter a num: "))
# temp = num
# rev = 0
# while num>0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if temp == rev:
#     print("Palidrome")
# else:
#     print("Not a palidrome")

#------Perfect number------
# num = int(input("Enter a num: "))
# Sum = 0
# for i in range(1, num ):
#     if num % i == 0:
#         Sum = Sum + i
# if Sum == num:
#     print("Its a perfect num")
# else:
#     print("Not a perfect num")

#-------Fibonnaci series ------
# def fibo(n):
#     a = 0
#     b = 1
#     for i in  range(0,n):
#         temp = a
#         a = b
#         b += temp
#     return(a)
# for c in range(0,10):
#     print(fibo(c))

#--------Prime num-------
# def prime(num):
#     list_prime =[]
#     j = 0
#     for n in range(1, num +1):
#         if n > 1:
#             for i in range(2,n):
#                 if (n%i ==0):
#                      break
#             else:
#                 list_prime.append(n)
#     print(list_prime)
    # if j== 2:
    #     return("True")
    # else:
    #     return("false")
# print(prime(10))

#-------Multipication Table--------
# def multiply(k):
#     for i in range(1,20+1):
#         print(k, "x", i, "=", i * k)
# multiply(int(input("Enter a number: ")))

def allmultiply(k):
    for i in range(1,k+1):
        print("\n\n")
        for n in range(1,20+1):
            print(i, "x", n, "=", i *n)
allmultiply(int(input("Enter a number: ")))