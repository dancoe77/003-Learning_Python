zz = "#######################################"
print(zz)

x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
print(zz)

# print(lambda int:int**2)
# GLOBAL
name = "This is a global string"

def greet():
    # ENCLOSING
    name = "Sammy"
    print(f"Hi {name}")

    def hello():
        # LOCAL
        name = "I'm a local"
        print(f"Hello {name}")
    hello()
greet()
print(name)
print(zz)

x = 50
def var(x):
    print(f"X is {x}")

    x = 200
    print(f"I just changed locally changed x to {x}")
var(x)
print(zz)

def var():
    global x
    print(f"X is {x}")

    x = 200
    print(f"I just locally changed global x to {x}")
var()
print(x)
print(zz)

y = 100
def var(y):
    print(f"Y is {y}")

    y = "New Value"
    print(f"I just locally changed global y to {y}")
    return y
print(y)
y = var(y)
print(y)
print(zz)