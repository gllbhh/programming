import math


def calculate_square_area(side_length):
    square_area = side_length ** 2
    return square_area
    # function code from the square assignment


def calculate_sector_area(circle_radius, sector_angle):
    # function code from the the sector assignment
    sector_area = circle_radius ** 2 * sector_angle * math.pi / 180 / 2
    return sector_area


def calculate_catheti_length(hypotenuse_length):
    # function code from the pythagoras assignment
    catheti = hypotenuse_length / 2 ** 0.5
    return catheti


def calculate_figure_area(x):
    # all calculations to get the area of the figure
    # are done inside this function, using the
    # other functions for intermediate results

    # main program that prompts for x,
    # calls the calculation function and
    # prints the rounded result
    # area = x ** 2 * (1.5625 * math.pi + 3.25)
    big_square_side = 2 * calculate_catheti_length(x)
    area = 1.25 * calculate_square_area(x) + calculate_square_area(big_square_side) + calculate_sector_area(
        big_square_side, 270) + calculate_sector_area(big_square_side / 2, 45)
    return round(area, 4)


x = float(input("x: "))
print("Figure area: ", calculate_figure_area(x))
