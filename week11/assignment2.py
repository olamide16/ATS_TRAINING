class Rectangle:
    def __init__(self,topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
    def area(self):
        return (self.topLeft + self.topRight) * (self.bottomLeft + self.bottomRight)
        
    def perimeter(self):
        return (2 * (self.topLeft + self.topRight)) * (2 *(self.bottomLeft + self.bottomRight))
        
    def position(self):
        return (self.topLeft, self.topRight, self.bottomLeft, self.bottomRight)
r1 = Rectangle(5,5,10,10)
# print(r1.area())
# print(r1.perimeter())
# print(r1.position())