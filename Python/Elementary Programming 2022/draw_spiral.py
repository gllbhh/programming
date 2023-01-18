from turtle import *


def draw_spiral(s_color, number_of_arcs, starting_radius, radius_growth, pen_weight=1):
    """ draw a spiral
        color - three value tuple or color string
        number_of_arcs - how many quarters of a circle to draw (int)
        starting_radius - starting radius (int)
        radius_growth - every step radius increse by this value (float)
        pen_weigh - default = 1"""
    color(s_color)
    pensize(pen_weight)
    radius = starting_radius
    for i in range(number_of_arcs):
        circle(radius, 90)
        radius += radius_growth


draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)
done()
