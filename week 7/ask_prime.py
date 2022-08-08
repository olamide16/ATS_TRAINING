num = int(input("Enter a number: "))
if num > 1:
    for i in range (2, (num //2) + 1):
        if num % i == 0:
            print(True)
        else:
            print(False)