class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name =  name

mydog = Dog(breed="Lab", name="sammy")
other_dog = Dog(breed="Husky", name="foxy")
print(type(mydog))
print(mydog.breed)
print(other_dog.name)