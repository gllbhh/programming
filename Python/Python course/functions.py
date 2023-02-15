"""Functions"""


def greet(firest_name, last_name):
    """My Function"""
    print(f"Hi {firest_name} {last_name}")
    print("Welcome abroad")


def get_greeting(name):
    return f"HI {name}"


def increment(number, by=1):
    # if default value is defined the parameter becomes optional
    return number + by


def multiply(*numbers):
    # * - allows to pass a multiple arguments to a function.
    # Values are stored in a touple
    total = 1
    for number in numbers:
        total *= number
    return (total)


def save_user(**user):
    # ** - allows to pass a dictionary to a function
    print(user["name"])
    print(user["age"])


greet("Gll", "Bhh")
print(greet("Gll", "Bhh"))
message = get_greeting("Gll")
file = open("content.txt", "w")
file.write(message)
print(increment(2, by=3))       # "by" is a keyword argument
print(multiply(2, 3, 4, 5))
save_user(id=1, name="John", age=22)


# *** Debugging tips
# Continue (F5) – this will run past the breakpoint
# and continue with the rest of the program until it hits the next breakpoint.
# Step over (F10) – this will take the debugger down to the following line.
# Step into (F11) – this will take the debugger into the following function.
# Step out (F12) – this will take the debugger out of the function
# and into the next step.
# Restart (Ctrl+shift+F5) – restart the entire debugger.
# Stop (shift+F5) – stop the debugging process and exit it.
# Add a debugging point (F9)
