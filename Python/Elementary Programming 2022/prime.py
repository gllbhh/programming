def check_prime(num):
    """
    Checks whether an integer is a prime number. Returns False
    if the number isn't a prime; if it is a prime, returns True

    """
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False


def prompt_input(message, error_message):
    """
    Prompts the user for an integer using the prompt parameter.
    If an invalid input is given, an error message is shown using
    the error message parameter. A valid input is returned as an
    integer. Only accepts integers that are bigger than 1.
    """
    while True:
        try:
            num = int(input(message))
        except ValueError:
            print(error_message)
        else:
            if num > 1:
                return num
            else:
                print(error_message)


user_input = prompt_input("Give an integer that's bigger than 1: ",
                          "You had one job")
if check_prime(user_input):
    print("This is a prime")
else:
    print("This is not a prime")
