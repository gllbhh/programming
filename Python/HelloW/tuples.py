# Tuple - read only list
from ctypes import pointer


point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")

x = 10
y = 11
x, y = y, x
print("X: ", x)
print("y: ", y)
