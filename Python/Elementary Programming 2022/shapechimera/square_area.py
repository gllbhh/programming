def calculate_square_area(side_length):
    square_area = side_length ** 2
    return round(square_area, 4)


side_length = float(input("side length: "))
print(calculate_square_area(side_length))
