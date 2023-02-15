def fizz_buzz(input):
    if int(input) % 3 == 0 and int(input) % 5 == 0:
        print("fizzbuzz")
    elif int(input) % 3 == 0:
        print("fizz")
    elif int(input) % 5 == 0:
        print("buzz")
    else:
        print(input)


fizz_buzz(input=21)
