def calculate_length(v):
    square = 0
    for component in v:
        square += component ** 2
    return square ** 0.5


def to_unit_vector(v):
    u = []
    length = calculate_length(v)
    # loop declaration
    # loop content block (1 line)
    for component in v:
        u.append(component / length)
    return u


print(to_unit_vector([2.0, 2.0, 2.0, 2.0]))
