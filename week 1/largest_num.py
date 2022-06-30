# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))
# e = int(input("Enter a number: "))

# number_list = [a,b,c,d,e]
# average= (a+b+c+d+e)//5
# print(number_list)
# print(average)
#number list that can calculate the average number of any number list given by a user
# n = int(input("Enter number"))
# sum = 0
# loop from 1 to n
# for num in range(1, n + 1, 1):
#     sum = sum + num
# print("Sum of first ", n, "numbers is: ", sum)
# average = sum / n
# print("Average of ", n, "numbers is: ", average)
input_string = input('Enter numbers separated by space ')
# print("\n")
numbers = input_string.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    print(numbers)

print(sum(numbers) / len(numbers))
