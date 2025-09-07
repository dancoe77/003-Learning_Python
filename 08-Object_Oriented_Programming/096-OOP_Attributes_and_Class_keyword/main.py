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
    def __init__(self,breed,name,spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        # Expect string
        self.breed = breed
        self.name = name
        # Expect boolean
        self.spots = spots
my_dog = Dog(breed="Lab",name="Sammy",spots=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(zz)

my_new_dog = Dog(breed="Huskie",name="Samoa",spots=False)
print(type(my_new_dog))
print(my_new_dog.breed)
print(my_new_dog.name)
print(my_new_dog.spots)
print(zz)