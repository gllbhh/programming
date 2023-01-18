def addition(num_1, num_2):
    """addition"""
    return num_1 + num_2


def subtraction(num_1, num_2):
    """subtraction"""
    return num_1 - num_2


def multiplication(num_1, num_2):
    """multiplication"""
    return num_1 * num_2


def division(num_1, num_2):
    """division"""
    return num_1 / num_2


action = input("Choose operation (+, -, *, /): ")
if action in ("+", "-", "*", "/"):
    try:
        number_1 = float(input("Give 1st number: "))
        number_2 = float(input("Give 2nd number: "))
    except ValueError:
        print("I don't think this is a number")
    else:
        if action == "+":
            print("result: ", addition(number_1, number_2))
        elif action == "-":
            print("result: ", subtraction(number_1, number_2))
        elif action == "*":
            print("result: ", multiplication(number_1, number_2))
        elif action == "/":
            try:
                print("result: ", division(number_1, number_2))
            except ZeroDivisionError:
                print("This program can't reach infinity")
else:
    print("Selected operation doesn't exist")
