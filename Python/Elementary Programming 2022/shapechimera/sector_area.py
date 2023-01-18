import math


def calculate_sector_area(circle_radius, sector_angle):
    # Sector_Area = r^2 * a / 2
    sector_area = circle_radius ** 2 * sector_angle * math.pi / 180 / 2
    return round(sector_area, 4)


radius = float(input("Radius: "))
angle = float(input("Sector Angle : "))
print("Sector area: ", calculate_sector_area(radius, angle))
