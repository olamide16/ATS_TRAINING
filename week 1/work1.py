# print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
# """This is a test Python program.
# Written by Al Sweigart al@inventwithpython.com
# This program was designed for Python 3, not Python 2.
# """
# def spam():
#  """This is a multiline comment to help
#  explain what the spam() function does."""
#  print('Hello!')
# spam()
# greetings = input("How are you? ")
# if greetings.lower() == 'great':
#     print("It's fine also")
# else:
#     print("Its okay")
while True:
 print('Enter your age:')
 age = input()
 if age.isdecimal():
     break
 print('Please enter a number for your age.')
while True:
 print('Select a new password (letters and numbers only):')
 password = input()
 if password.isalnum():
    break
 print('Passwords can only have letters and numbers.')