zz = "#######################################"
print(zz)

#class Animal():
#    def __init__(self):
#        print("Animal Created")
#    def who_am_i(self):
#        print("I am an animal")
#    def eat(self):
#        print("I am eating")
# myanimal = Animal()
# myanimal.who_am_i()
# myanimal.eat()
# print(zz)

#class Dog(Animal):
#    def __init__(self):
#        Animal.__init__(self)
#        print("Dog Created")
#    def who_am_i(self):
#        print("I am a dog")
#    def eat(self):
#        print("I am a dog and eating")
#    def bark(self):
#        print("Woof!")
#mydog = Dog()
#mydog.who_am_i()
#mydog.eat()
#mydog.bark()
#print(zz)

class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"
niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())
print(felix.speak())
print(zz)

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))
print(zz)

def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
print(zz)

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
# myanimal = Animal("Fred")
# myanimal.speak()
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"
class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"
fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())
print(zz)