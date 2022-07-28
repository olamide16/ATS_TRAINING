# from opcode import opname
# from tkinter import Y
# def linux_interaction():
#     linux = input

# try: 
#     linux_interaction()
#     with open('file.py') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print("fnf_error  \npass")
# except AssertionError as error:
#     print(error)
#     print('linux linux_interaction() function was not excuted')
# from logging import exception


# a = 5
# b = 0
# try: 
#     # print(a/b )
#     key = int(input("Enetr an interger: "))
#     print(key)
# except ValueError as e:
#     print("invalid input")
# except ZeroDivisionError as e:
#     print("Your cannot divide a  number by zero")
# except Exception as e:
#     print("sometin went wrong")    
# finally:
#     pass
    
# print('bye ')
# obejctv orientation program
# from shutil import move


# class Point:
#     def __init__(self) -> None:
#         pass
    
    
#     def move(self):
#         print("move")
        
        
#     def draw(self):
#         print("draw")
        
# Point1 = Point()
# Point1.x = 10
# Point1.y = 20
# print(Point1.x,Point1.y)

# point2 = Point()
# point2.x = 10
# print(point2.x )
# Point1.move() 



# constructor
# from textwrap import fill


# class Point():
#     def move(self):
#         print("move")
        
        
#     def draw(self):
#         print("draw")
# try: 
#     point = Point()
#     print(point.x)
# except AttributeError as e:
#     print("Object attribute not found")
# finally:
#     pass

# class Point():
#     def __init__(self,x,y):
#         self.x =x 
#         self.y =y
#     def move(self):
#         print("move")
        
        
#     def draw(self):
#         print("draw")
# point = Point(10,20)
# print(point.x)
# print(point.y)

# class Person():
#     def __init__(self,name):
#         self.name = name
    # def Name(self):
        # pass
#     def Talk(self):
#         print(f"Hi , I am {self.name}")
# john = Person("John Smith")
# john.Talk()
# # john.Talk( )
# bob = Person("Bob Smith")
# bob.Talk()

# inheritance 
# from ast import walk

# class Mammal:
#     # def __init__(self,animal):
#     #     self.animal = animal
        
   
#     def walk(self):
#         print("walk")
        
        
# class Dog(Mammal):
#     def bark(self):
#         print("bark") 


# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
        

# dog =  Dog()
# dog.bark()
# cat = Cat()
# cat.walk()
# cat1 = Cat()
# cat1.be_annoying()
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
        
        
#     def print(self):
#         print(self.firstname, self.lastname)
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
    
    
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname," to the class of",self.graduationyear)

# x = Student("john",'doe',2019)
# x.welcome()


# item1 = "Phone"
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))
# class Item:
#     def __init__(self,name: str,price: float,quantity: int) -> None:
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def calculate_total_price(self):
#         return self.price * self.quantity
#         pass 
        
    
    
# item1 = Item("Phone","100",5)
# print(item1.calculate_total_price())


# item2 = Item("Laptop","1000",3)
# item2.has_numpad = False
# print(item2.calculate_total_price())
# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(type(item1))
# print(type(item1.price))
# print(type(item1.quantity))
class Item:
    def __init__(self,name: str,price: float,quantity: int) -> None:
        
        assert price >= 0,f"Price {price} is not greater than or equal to  zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to that zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
        pass 

item1 = Item("Phone",100,-5)
print(item1.calculate_total_price())
# item2 = Item("Laptop",1000,3)
# print(item2.calculate_total_price())