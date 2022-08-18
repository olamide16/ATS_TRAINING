import cmath
import string
import random
from fractions import Fraction

alphabets = list(string.ascii_letters)
cap_alphabets = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
count = list (alphabets + digits + special_characters + characters+cap_alphabets)

def random_password():
    length = 10
    random.shuffle(count)
    # if count == len
    # for i in range()
    # if  len(count) == 8:
        # for i in range()
    
    password = []
    for i in range (length):
        password.append(random.choice(count))
    
    random.shuffle(password)
    print("".join(password))
    
# random_password()

def hangman():
    list_hangman= ["Letter", "Happiness","Backend", "House", "Pneumonoultramicroscopicsilicovolcanoconiosis", "Methionylthreonylthreonylglutaminylarginyl", "Supercalifragilisticexpialidocious", "Pseudopseudohypoparathyroidism", "Antidisestablishmentarianism", "Aequeosalinocalcalinoceraceoaluminosocupreovitriolic"]  
    word = random.choice(list_hangman)
    fail = 10
    letter_guessed = ""
    while fail > 0:
        # print("_", end="")
        guess = input("\nEnter a letter: ")
        
        if guess in word:
            pass
        else:
            fail -= 1
            print("Not in the word")
        
        letter_guessed =  letter_guessed + guess
        wrong = 0
        
        for letter in word:
            if letter in letter_guessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrong += 1
        
        if wrong == 0:
            # print(f"{word}")
            print(f"\nYou won!")
            break
        # elif wrong == 2:
            # print(f"\nYou Lose!")
        # else:
            # print(f"\nYou Lose!")
            # break
# hangman()

def complex_number():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    complex_num = complex(x,y)
    print(cmath.phase(complex_num))
# complex_number()

def guess_game():
    # num = random.randint(1,10)
    # guess = 0
    # while guess != num:
    number = random.randint(1, 10)
    num_of_guesses = 0
    while num_of_guesses < 5:
        guess = int(input("Enter your guess number: "))
        num_of_guesses += 1
        if guess != number:
            print("Incorrect guess")
        elif guess == number:
            break
        
    if guess == number:
        print(f"{guess} \nGreat You Won!")
    else:
        print(f"{guess} \nYou Lost!")
# guess_game()

def rational_number(x, y):
    num = Fraction(x, y)
    print(num)
# rational_number(3, 7)

def cardinal_number(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

    if n < 0:
        n *= -1

    n = int(n)

    if n % 100 in (11,12,13):
        s = 'th'
    else:
        s = suffix[n % 10]

    return str(n) + s
# print(cardinal_number(int(input("Enter a number: "))))

def calculate():
    print(""" 
          multiplying - *
          addition - +
          subtration - -
          division - / for decimal point
          square - **
          """) 
    find = eval(input("Enter ur calculation: "))
    find2 = int(find)
    print(find2)
    
# calculate()
