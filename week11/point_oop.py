from decimal import Decimal
import random


class Point:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
        
    
    def show(self):
        if self.x0<-181 and self.x0< 180 and self.y0<-181 and self.y0< 180:
            return (self.x0, self.y0)
        else:
            return ("Invalid input")
    
    def move_random(self):
       self.x0 = random.randint(-180,180)
       self.y0 = random.randint(-180,180)
       return (self.x0, self.y0)
   
    def move(self, x01, y01):
        self.x01 = x01 + self.x0
        self.y01 = y01 + self.y0
        if self.x01<-181 and self.x01< 180 and self.y01<-181 and self.y01< 180:
            return (self.x01, self.y01)
        else:
            return ("Invalid in put") 
    
    def dist(self, x1, y1):
        self.y1 = x1
        self.x1 = y1
        return ((self.x1 - self.x0)**2 + (self.y1 - self.y0) ** 2)** 1/2
    
    def __str__(self) -> str:
        return (self.x0, self.y0)
p1 = Point(2,3)
p2 = Point(310,3)
# print(p1.move(10,-10))
# print(p1.dist(11,15))
print(p1.show())
# print(p2.show())
# print(p1.show())
# print(p1.dist(3,3))