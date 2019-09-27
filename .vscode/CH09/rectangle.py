class Rectangle:
    """Holds with and length and calculates area."""
    area_formula="area = length * width"
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
new_rectangle= Rectangle(12,10)
print(new_rectangle.area())
print(new_rectangle.area_formula)
rect2=Rectangle(6,8)
print(rect2.area_formula)

