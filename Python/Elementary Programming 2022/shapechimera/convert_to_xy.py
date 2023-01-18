import math


def convert_to_xy(angle_radians, ray):
    # To convert from Polar Coordinates (r,θ)
    # to Cartesian Coordinates (x,y) :
    # x = r × cos( θ )
    # y = r × sin( θ )
    x = ray * math.cos(angle_radians)
    y = ray * math.sin(angle_radians)
    return int(round(x)), int(round(y))


print(convert_to_xy(1.5708, 1))
