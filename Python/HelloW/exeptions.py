from msilib.schema import Error


try:  # a way to handle error messages
    file = open("app.py")  # if you open a file you need to close it!!!
    age = int(input("Age: "))
    xfactor = 1/age
except ValueError as ex:  # in case of exception print an error message and store error message in variable "ex"
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except (ZeroDivisionError, ZeroDivisionError):  # to add the same message to several error messages
    print("Age can not be 0.")
else:
    print("No exeptions were thrown.")
finally:  # part which will be execuited anyway
    file.close()


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
