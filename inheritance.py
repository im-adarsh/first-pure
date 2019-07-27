# base class
class Animal():
    def __init__(self):
        print("animal created")

    def who_am_i(self):
        print("animal")

    def eat(self):
        print("eating")

# calling base class
mya = Animal()
mya.who_am_i()
mya.eat()

# child class
class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print("dog created")

    def eat(self):
        print("dog eating")

    def bark(self):
        print("whoof")

# initializing and calling child class
myd = Dog()
myd.who_am_i()
myd.eat()
myd.bark()
