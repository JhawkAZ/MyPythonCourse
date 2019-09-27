import math
class Circle:
    
    """calculates the area of a circle"""
   
    def __init__(self,radius):

        self.radius=radius
    def area(self):
        return 2*math.pi*self.radius

circle1=Circle(6)

print(circle1.area())


class Rectangle:
    """returns the area of a rectangle"""
    def __init__(self,length,width):
        self.witdh=width
        self.length= length
    