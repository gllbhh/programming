def length():
    print("Select unit of length from the options below using the abbreviations")
    print("Inch (in or \")")
    print("Foot (ft or ')")
    print("Yard (yd)")
    print("Mile (mi)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "in" or unit == "\"":
        print("{us_value:.2f}\" is {si_value:.2f} cm".format(
            us_value=value, si_value=value * 2.54))
    elif unit == "ft" or unit == "'":
        print("{us_value:.2f}' is {si_value:.2f} cm".format(
            us_value=value, si_value=value * 39.48))
    elif unit == "yd":
        print("{us_value:.2f} yd is {si_value:.2f} m".format(
            us_value=value, si_value=value * 0.9144))
    elif unit == "mi":
        print("{us_value:.2f} mi is {si_value:.2f} km".format(
            us_value=value, si_value=value * 1.609344))
    else:
        print("The selected unit is not supported")


def mass():
    print("Select unit of mass from the options below using the abbreviations")
    print("Ounce (oz)")
    print("Pound (lb)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "oz":
        print("{us_value:.2f} oz is {si_value:.2f} g".format(
            us_value=value, si_value=value * 28.349523125))
    elif unit == "lb":
        print("{us_value:.2f} lb is {si_value:.2f} kg".format(
            us_value=value, si_value=value * 0.45359237))
    else:
        print("The selected unit is not supported")


def volume():
    print("Select unit of mass from the options below using the abbreviations")
    print("Cup (cp)")
    print("Pint (pt)")
    print("Quart (qt)")
    print("Gallon (gal)")
    unit = input("Input source unit: ")
    value = float(input("Input value to convert: "))
    if unit == "cp":
        print("{us_value:.2f} cp is {si_value:.2f} dl".format(
            us_value=value, si_value=value * 2.365882365))
    elif unit == "pt":
        print("{us_value:.2f} pt is {si_value:.2f} dl".format(
            us_value=value, si_value=value * 4.73176473))
    elif unit == "yd":
        print("{us_value:.2f} qt is {si_value:.2f} l".format(
            us_value=value, si_value=value * 0.946352946))
    elif unit == "mi":
        print("{us_value:.2f} gal is {si_value:.2f} l".format(
            us_value=value, si_value=value * 3.785411784))
    else:
        print("The selected unit is not supported")


def temperature():
    print("Temperature conversion from Fahrenheit to Celsius.")
    fahrenheit = float(input("Input temperature: "))
    celcius = (5 / 9) * (fahrenheit - 32)
    print("{us_value:.2f} °F is {si_value:.2f} °C".format(
        us_value=fahrenheit, si_value=celcius))


print("This program converts US customary units to SI units")
print("Available features:")
print("(l)ength")
print("(m)ass")
print("(v)olume")
print("(t)emperature")
print()
choice = input("Make your choice: ").strip().lower()
if choice == "length" or choice == "l":
    length()
elif choice == "mass" or choice == "m":
    mass()
elif choice == "volume" or choice == "v":
    volume()
elif choice == "temperature" or choice == "t":
    temperature()
else:
    print("The selected feature is not available")
