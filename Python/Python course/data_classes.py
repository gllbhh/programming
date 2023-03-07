from collections import namedtuple


# if we have a data only class we can use a namedtuple method instead
# this way we dont need to define magic methods for a class ==> less code

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(id(p1))
# atribute in a namedtuple is not immutable
# so p1.x = 10 won't work
# to changa an atribute we'll need to initialise a tuple againg
p1 = Point(x=10, y=2)
print(p1.x)
print(id(p1))
p2 = Point(x=1, y=2)
print(p1 == p2)
