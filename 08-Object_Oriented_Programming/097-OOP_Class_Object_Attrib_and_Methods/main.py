zz = "###############################################"
print(zz)

mylist = [1,2,3]

myset = set()
print(type(myset))
print(type(mylist))
print(zz)

class Sample():
    pass
my_sample = Sample()
print(type(my_sample))
print(zz)

class Dog():
    # Class object attribute
    # Same for any instance of a class
    species = "mammal"

    def __init__(self,breed,name,spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        # Expect string
        self.breed = breed
        self.name = name
        # Expect boolean
        self.spots = spots
    # Operations/Actions -> Methods
    def bark(self,age):
        print("Woof! My name is {} and I'm {} years old".format(self.name,age))
my_dog = Dog("Lab","Sammy",False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.species)
print(my_dog.name)
print(my_dog.spots)
my_dog.bark(7)
print(zz)

my_new_dog = Dog("Huskie","Samoa",False)
print(type(my_new_dog))
print(my_new_dog.breed)
print(my_new_dog.species)
print(my_new_dog.name)
print(my_new_dog.spots)
my_new_dog.bark(2)
print(zz)

class Circle():
    # Class Object Attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    # Method
    def get_curcumference(self):
        return self.radius * self.pi * 2
    def get_area(self):
        return self.radius * self.radius * self.pi
my_circle = Circle(30)
print(type(my_circle))
print(my_circle.radius)
print(my_circle.pi)
print(my_circle.get_curcumference())
print(my_circle.get_area())
print(zz)