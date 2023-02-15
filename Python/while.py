"""While loop"""
number = 100 
while number > 0:
    print(number)
    number //= 2


command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


while True:
    command2 = input(">")
    print("ECHO", command)
    if command2.lower() == "quit":
        break