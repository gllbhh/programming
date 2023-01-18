try:
    distance = float(input("Input distance traveled (m):"))
    time = float(input("IInput elapse time (s):"))
except ValueError:
    print("You need less donuts, and more number inputting.")
else:
    print(
        f"The speed of a car traveling {distance: .2f} meters"
        f"in {time: .2f} seconds is {distance / time * 3.6: .2f} km/h"
    )
