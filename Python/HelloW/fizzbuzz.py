def fizz_buzz(input):
    if not int(input) % 3 and not int(input) % 5:
        return "fizzbuzz"
    if not int(input) % 5:
        return "buzz"
    if not int(input) % 3:
        return "fizz"
    return input


print(fizz_buzz(15))
