num = int(input("Enter a number:"))

def perfect_number(n):
    sum=0
    for x in range(1,n):
        if n%x == 0:
            sum +=x
    if sum == n:
        print("Perfect number.")
    else:
        print("Not a perfect number.")


perfect_number(num)