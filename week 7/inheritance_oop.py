# class Person:
#     def __init__(self,fname,lname):
#         self.first_name = fname 
#         self.last_name = lname 
        
        
#     def printname(self):
#         print(f"firstname is {self.first_name} and last name {self.last_name}")


# class Student(Person):
#     pass
# x = Student("Adewale","Ademide")
# x.printname()

from cmath import sqrt


class Shapes:
    def __init__(self,no_of_lenght,lenght) -> None:
        self.no_of_lenght = no_of_lenght
        self.lenght = lenght
    
class Triangle(Shapes):
        def __init__(self, base, height,scalence_last_side) -> None:
            self.base = base
            self.height = height
            self.scalence_last_side = scalence_last_side
            
            
        def area(self):
                # triangle_type = """
                # 1. Scalene Triangle
                # 2. Isoscele Triangle
                # 3. Equilateral Triangle"""
                # if triangle_type == 2:
                #     0.5(self.base * self.height)
                # elif triangle_type == 3:
                #     (sqrt(0.75) * (self.height) ** 2)
                # elif triangle_type == 1:
                #     0.5(self.base * self.height)
                return 0.5*(self.base * self.height)
        
        
        def perimeter(self):
                # triangle_type = """
                # 1. Scalene Triangle
                # 2. Isoscele Triangle
                # 3. Equilateral Triangle"""
                # if triangle_type == 1:
                #     self.base + self.height + self.scalence_last_side
                # elif triangle_type == 2:
                #     2(self.height) + self.base
                # elif triangle_type == 3:
                #     3(self.height)
                return self.base + self.height + self.scalence_last_side