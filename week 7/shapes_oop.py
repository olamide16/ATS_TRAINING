from cmath import sqrt
import math


class Shape:
    # def __init__(self,side) -> None:
    #     self.side = side
        pass


class TwoDimensionalShape(Shape):
    pass


class ThreeDimensionalShape(Shape):
    pass


class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Square(TwoDimensionalShape):
    def __init__(self, length):
        self.length = length
        
    def calculate_area(self):
        return self.length ** 2
    
    def calculate_perimeter(self):
        
        return 4 * self.length


class Triangle(TwoDimensionalShape):
    def __init__(self, base, height, slant_height):
        self.base = base
        self.height = height
        self.slant_height = slant_height

    def calculate_area(self):
        return 0.5 * (self.base + self.height)
    
    def calculate_perimeter(self):
        return 2 * (self.slant_height + self.base)


class Sphere(ThreeDimensionalShape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def calculate_volume(self):
        return 0.33 * math.pi * (self.radius ** 3)


class Cube(ThreeDimensionalShape):
    def __init__(self, side1):
        self.side1 = side1

    def calculate_perimeter(self):
        return 12 * self.side1
    
    def calculate_volume(self):
        return self.side1 ** 3

    def calculate_area(self):
        return 6 * (self.side1 ** 2)


class Tetrahedron(ThreeDimensionalShape):
    def __init__(self, side1):
        self.side1 = side1

    def calculate_area(self):
        return math.sqrt(3) * (self.side1 ** 2)

    def calculate_volume(self):
        return (self.side1 ** 3)/ 6 * (math.sqrt(2))

    def calculate_perimeter(self):
        return 6 * self.side1


class Tarpezium(TwoDimensionalShape):
    def __init__(self, side1, side2, side3, side4, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.height = height

    def calculate_area(self):
        return ((self.side1 + self.side2)/ 2) * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4


class Rhombus(TwoDimensionalShape):
    def __init__(self, side, diagonal1, diagonal2):
        self.side = side
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def calculate_area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def calculate_perimeter(self):
        return 4 * self.side


class Parallelogram(TwoDimensionalShape):
    def __init__(self, slant_height, base,height):
        self.slant_height = slant_height
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        return 2 (self.slant_height + self.width)

    def calculate_area(self):
        return self.height * self.base


class Kite(TwoDimensionalShape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return self.side1 * self.side2 * math.sin(self.side1)
    
    def calculate_perimeter(self):
        return 2 * (self.side1 + self.side2)


class Rectangle(TwoDimensionalShape):
    def __init__(self, width, length):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    
    def calculate_area(self):
        return self.width * self.length


class Pentagon(TwoDimensionalShape):
    def __init__(self, side, apothem):
        self.side = side
        self.apothem = apothem
    
    def calculate_area(self):
        return 0.5 * (5 * self.side) * self.apothem
    
    def calculate_perimeter(self):
        return 5 * self.side


class Hexagon(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return (3 * math.sqrt(3))/ 3 * (self.side ** 2)

    def calculate_perimeter(self):
        return 6 * self.side


class Octagon(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return 2 * (1 + math.sqrt(2)) * self.side ** 2

    def calculate_perimeter(self):
        return 8 * self.side 


class Nonagon(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 9 * self.side
    
    def calculate_area(self):
        return (9/4) * (self.side ** 2 * 1/(math.tan) * math.pi/9)
        

class Decagon(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 10 * self.side
    
    def calculate_area(self):
        return (5/2 * self.side ** 2) * math.sqrt(5 + 2) * (math.sqrt(5)) 


class RectangularPrism(ThreeDimensionalShape):
    pass


class Cylinder(ThreeDimensionalShape):
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    
    def calculate_perimeter(self):
        return (4 * self.radius) + (2 * self.height)

    def calculate_volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def calculate_area(self):
        return (2 * math.pi * self.height) + (2 * math.pi * (self.radius ** 2))


class  Cone(ThreeDimensionalShape):
    def __init__(self, height, radius):
        self.height = height 
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius (self.radius + math.sqrt((self.height ** 2)+ (self.radius ** 2)))

    def calculate_volume(self):
        return math.pi * (self.radius ** 2) * (self.height / 3)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
