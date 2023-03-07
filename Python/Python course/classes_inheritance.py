class Animal:
    def __init__(self):
        self.age = 2

    def eat(self):
        print("eat")

# Animal: Parent, Base class
# Mammal: Child, Sub Slass


class Mammal(Animal):
    def __init__(self):
        # call for a Animal class constructor instead of overwriting it
        # if super().__iniit__() is removed, only Mammal constructor will be used
        super().__init__()
        self.weight = 15

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


dog = Mammal()
dog.eat()
dog.walk()
print(dog.age)
print(dog.weight)

sig = Fish()
sig.swim()
print(isinstance(dog, Mammal))
print(isinstance(dog, Animal))
# all classes inherit class object
print(isinstance(dog, object))
