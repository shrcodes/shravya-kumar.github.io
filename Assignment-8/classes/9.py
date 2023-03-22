#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.14 * self.radius
NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())