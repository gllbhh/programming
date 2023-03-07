# Class: blueprint for creating new objects
# Object: instance of a class

class Point:
    # default value for every instance of a class
    default_color = "red"

    # object atributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class method
    # this one when colled creates an object (0, 0) of Point class
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # by default magic method __str__ returns object's class
    # and memory address
    def __str__(self):
        return f"({self.x}, {self.y})"

    # redefine magic method __eq__
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # define > operation for objects
    # < method will be understood automatically
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# create an object using class method
point = Point.zero()
# call for a method
point.draw()
print(point)
# create an object of class Point
point1 = Point(10, 20)
point2 = Point(1, 2)
print(point1 < point2)
print(point1 + point2)
