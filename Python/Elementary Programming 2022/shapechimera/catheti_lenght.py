from cmath import sqrt
import math


def calculate_catheti(hypotenuse_length):
    catheti = hypotenuse_length / math.sqrt(2)
    return round(catheti, 4)


hypotenuse = float(
    input("Input the hypotenuse length of a right isosceles triangle: "))
print("Catheti length: ", calculate_catheti(hypotenuse))
