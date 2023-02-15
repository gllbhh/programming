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
