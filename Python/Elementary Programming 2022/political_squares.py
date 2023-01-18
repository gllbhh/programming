from turtle import *


def draw_square(side, x, y):
    # write a function that draws a draws
    # a square with either red or blue fill
    # depending on the starting x position
    # being positive (blue) or negative (red)
    if x < 0:
        color('red')
    else:
        color('blue')

    up()
    setx(x)
    sety(y)
    down()
    begin_fill()
    for a in range(4):
        forward(side)
        right(90)
    end_fill()


draw_square(40, -100, 100)
draw_square(60, 100, -100)
draw_square(100, -50, -20)
draw_square(80, 90, 30)
done()
