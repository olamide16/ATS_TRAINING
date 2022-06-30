from cgitb import text
# Write a function that takes a two strings as an argument and prints if the first string is a substring of the second.
def substring(str1, str2):
    if str1 in str2:
        print("str1")
    else:
        print("they are not sunstring")
substring("counting", "count")
# Write a function that converts a string to uppercase and returns the result.
def uppercase(text):
    text = text.upper()
    return text
# Write a function that converts a string to lowercase and returns the result.
def lowercase(text):
    text = text.lower()
    return text
# Write a function that converts a string to titlecase and returns the result.
def titlecase(text):
    text = text.title()
    return text
# Write a function that converts the first letter of each word in a sentence to uppercase.
def firstChild():
    text = text.title()
    return text
# Write a function that checks if a string contains both alphabets and numbers
def isalnum(text):
    if text.isalnum():
        return True;
    else:
        return False;
