class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @ classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point_1 = Point(1, 2)
point_1.draw()
print(point_1.default_color)
print(Point.default_color)
Point.default_color = "yellow"
point_2 = Point(1, 2)
point_2.draw()
print(point_2.default_color)
point_3 = Point.zero()
point_3.draw()


print(point_1 < point_2)
combined = point_1 + point_2
print(combined)
print(point_1 + point_2)
