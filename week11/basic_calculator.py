def add(x,y):
    return x + y

def subract(x,y):
    return y - x

def multiply(x , y):
    return x * y

def division(x,y):
    return y/ x

        # OR
    # To calculate any number use this 
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
    
calculate()


# print(division(2,8))