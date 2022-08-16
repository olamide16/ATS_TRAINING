import random

guess_num = random.randint(1,10)
guess_count = 0
guess_limit = 5
# print(guess_num)
while guess_count < 2:
    guess = input("Enter a number btw 1 - 10: ")
    guess_count += 1
    if guess == guess_num:
        print("You get the guess num right")
        break
    else:
        print("U are unable to get the guess number right' ")
        print(guess_num)