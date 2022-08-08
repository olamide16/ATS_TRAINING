# from operator import itemgetter

# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

# l = []
# while True:
#     # s = input()
#     if not s:
#         break 
#     l.append(tuple(s.split(",")))
# print (sorted(l,key=itemgetter(0,1,2)))


# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# class MyGen:
#     def by_seven(self,n):
#         for i in range (0, int(n/7) + 1):
#             yield i * 7

# for i in MyGen().by_seven(int(input("Plz enter a number: "))):
    # print(i)


# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# frequency = {}
# line = input("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
# for word in line.split():
#     frequency[word] = frequency.get(word, 0) + 1

# words = frequency.keys()
# words.sort()

# for w in words:
#     print( "%s:%d" %(w,frequency[w]))
# ss = input("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.").split()
# word = sorted(set(ss))     # split words are stored and sorted as a set

# for i in word:
    # print("{0}:{1}".format(i,ss.count(i)))


# Write a method which can calculate square value of number

def square(num):
    return num ** 2
# print (square(2))

def SumFunction(number1, number2):
    return number1 + number2
# print (SumFunction(5,6))

def int_to_string(num):
    return str(num)
# print(int_to_string(7))

def printDict():
    d = dict()
    for i in range(1,21):
        d[i] = i ** 2
    # print (d)
# printDict()

def Dict():
    dict ={i: i**2 for i in range(1,21) }
    # print(dict)
# Dict()

li = [1,2,3,4,5,6,7,8,9,10]
suqaredNumbers = list(map(lambda x: x **2, li))
# print (suqaredNumbers)

li = [1,2,3,4,5,6,7,8,9,10]
evenNumber = list(map(lambda x: x ** 2, filter(lambda x: x%2 == 0, li)))
# print (evenNumber)

evenNumber = list(filter(lambda x: x%2 ==0, range(1,21)))
# print(evenNumber)

Number = list(map(lambda x: x**2, range(1,21)))
# print(Number)


email = "john@gmail.com"
email = email.split("@")
# print(email[0])

num = int(input("Enter a number: "))
sum = 0
for i in range(1,num +1):
    sum += float(float(i)/(i+ 1))
# print(sum)


def f(n):
    if n <=0:
        return 0
    else:
        return f(n -1) + 100
# n = int(input("Enter a number: "))
# print(f(n))

def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)
# n= int(input("Enter a number: "))
# print(f(n))
li = [2,4,6,5,8]
# for i in li:
    # assert i %2 == 0
    # print(li)




