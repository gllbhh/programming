def prompt_password():
    """promt password"""
    while True:
        password = input("Write password: ")
        if len(password) >= 8:
            return password
        print("The password must be at least 8 characters long.")


print(prompt_password())
