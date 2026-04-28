class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__ (self, length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
c = Circle(5)
r = Rectangle(4,6)

print("Area of Circle: ",c.area())
print("Area of Rectangle: ",r.area())
'''
OUTPUT:-
Area of Circle:  78.5
Area of Rectangle:  24
'''