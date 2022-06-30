# Write a function that takes a two strings as an argument and prints if the first string is a substring of the second.
# def substring(f_name,l_name):
def Substring(s1, s2):
    s1 = "good"
    s2 = "gooder"
    if s1 in s2:
      print( s2.index(s1))
    else:
        print("Not a substring")
