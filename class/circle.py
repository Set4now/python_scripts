import math
class Circle():
    
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * math.pi
    def perimeter(self):
        return math.pi * (self.radius**2)
a=Circle(5)
print (a.area())
print (a.perimeter())
