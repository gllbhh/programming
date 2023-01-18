m_points = [
    10.000, 10.244, 10.429, 10.576, 10.589, 10.606, 10.714, 10.794, 10.879, 10.99,
    11.263, 11.448, 11.596, 11.836, 11.869, 11.936, 12.174, 12.182, 12.243, 12.282,
    12.285, 12.297, 12.363, 12.417, 12.629, 12.71, 12.816, 13.138, 13.153, 13.215,
    13.27, 13.32, 13.367, 13.368, 13.923, 13.97, 14.171, 14.204, 14.235, 14.382,
    14.481, 14.581, 14.588, 14.645, 14.7, 14.704, 14.711, 14.803, 14.936, 15.000
]
m_values = [
    30.4, 74.165, 118.615, 54.293, 174.187, 162.399, 25.643, 181.571, 151.84, 147.307,
    85.115, 81.337, 65.852, 127.676, 10.409, 131.279, 32.595, 89.49, 40.263, 32.712,
    114.974, 7.967, 131.166, 124.827, 172.936, 145.234, 156.433, 118.446, 2.253, 69.263,
    99.249, 23.344, 119.2, 169.069, 187.976, 113.63, 173.847, 193.978, 54.206, 60.27,
    199.026, 167.434, 138.631, 3.259, 23.886, 88.825, 49.804, 109.179, 62.388, 126.052
]


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


def find_indices(points, min_boundary, max_boundary):
    """
    Finds two endpoints from a list of numerical data so that the resulting
    the values between the selected indices are between the given minimum 
    and maximum boundaries. Returns the two indices.
    """
    min_in = find_first(points, min_boundary)
    max_in = find_last(points, max_boundary)

    return min_in, max_in


def find_first(list, min_val):
    """
    Finds first element of the list that is 
    greater or equal than given value
    """
    if min_val >= list[-1]:
        return len(list)
    index = 0
    while min_val > list[index]:
        index += 1
    return index


def find_last(list, max_val):
    """
    Finds element of the list that is 
    greater than given value
    """
    if max_val >= list[-1]:
        return len(list)
    index = 0
    while max_val >= list[index]:
        index += 1
    return index


start_slice, end_slice = prompt_two_numbers(
    "Give two measurement points separated by space: ")
min_index, max_index = find_indices(m_points, start_slice, end_slice)
print("Measured values in the selected range: ")
print(m_values[min_index:max_index])
