def calculate_parameters(x_1, y_1, x_2, y_2):
    """Calculate line's slope m = (y2 - y1) / (x2 - x1) 
    and line's y intercept b = (x2 * y1 - x1 * y2) / (x2 - x1)"""
    m = (y_2 - y_1) / (x_2 - x_1)
    b = (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1)
    return m, b


try:
    x_point_1 = float(input("x coordinate of the first point: "))
    y_point_1 = float(input("y coordinate of the first point: "))
    x_point_2 = float(input("x coordinate of the second point: "))
    y_point_2 = float(input("y coordinate of the second point: "))
except ValueError:
    print("numbers only pls")
else:
    if x_point_1 == x_point_2 and y_point_1 == y_point_2:
        print("Sorry to break it to you but these points are the same.")
    elif x_point_1 == x_point_2 and y_point_1 != y_point_2:
        print("The line is vertical, it doesn't have an equation.")
    else:
        slope, intercept = calculate_parameters(
            x_point_1, y_point_1, x_point_2, y_point_2)
        if intercept == 0:
            print(f"Line equation:: y = {slope:.3f}x")
        elif intercept < 0:
            print(f"Line equation:: y = {slope:.3f}x - {abs(intercept):.3f}")
        else:
            print(f"Line equation:: y = {slope:.3f}x + {intercept:.3f}")
