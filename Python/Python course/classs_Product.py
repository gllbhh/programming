class Product:
    def __init__(self, price):
        # self.set_price(price) - before we created property
        # same thing using created property
        self.price = price

    # creates an property object
    # same as price = property(...)
    @property
    def price(self):
        return self.__price

    # "Unpythonic" implimetation. Use property fuction instead
    # if there's no setter method price will be read only
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # we can set methods to property function
    # fget - function how to read object's property
    # fset - function how to set object's property
    # fdel - function how to delete object's property
    # doc - function for socumenting
    # it's possibl;e to use not all of them
    # price = property(get_price, set_price)
    # val = property()


product = Product(50)
product.price = 100
print(product.price)
