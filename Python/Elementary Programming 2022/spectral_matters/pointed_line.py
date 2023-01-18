x_axis = [
    0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5,
    2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0
]


def calculate_parameters(p_1, p_2):
    """
    Calculate line's slope = (y2 - y1) / (x2 - x1) 
    and line's y intercept b = (x2 * y1 - x1 * y2) / (x2 - x1)
    """
    x_1, y_1 = p_1
    x_2, y_2 = p_2
    slope = (y_2 - y_1) / (x_2 - x_1)
    y_intercept = (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1)
    return slope, y_intercept


def prompt_two_numbers(message=""):
    """
    Prompts two floats from the user, separated by a space. The prompt
    is repeated until the user gives a valid input. Both numbers are
    returned as floats.
    """
    while True:
        try:
            numbers = input(
                message).split(" ")
            num_1 = float(numbers[0])
            num_2 = float(numbers[1])
        except (ValueError, TypeError, IndexError):
            print("Give two numbers separated by a space")
        else:
            if len(numbers) < 3:
                return num_1, num_2
            else:
                print("Give two numbers separated by a space")


def determine_points(line_slope, line_y_intercept, x_values):
    """
    Produces a list of values that are the y values of a line with
    the given slope and y intercept, from a list of x values.
    """
    y_values = []
    for x in x_values:
        y_values.append(x * line_slope + line_y_intercept)
    return y_values


point_1 = prompt_two_numbers("Input first point: ")
point_2 = prompt_two_numbers("Input second point: ")
line_slope, line_y_intercept = calculate_parameters(point_1, point_2)
y_axis = determine_points(line_slope, line_y_intercept, x_axis)
for y in y_axis:
    print("{:.4f}".format(y), end=" ")
