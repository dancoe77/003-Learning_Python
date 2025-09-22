zz = "######################################"
print(zz)

#@some_decorator
#def simple_func():
    # Do simple stuff
#    return something

def func():
    return 1
print(func())
print(zz)

def hello():
    return "Hello Nebula"
print(hello())
print(zz)

greet = hello
print(greet())
print(zz)

del hello
# print(hello())
print(greet())
print(zz)

del greet
def hello(name="Todd"):
    def greet():
        return "\t This is the greet() func inside hello"
    def welcome():
        return "\t This is welcome() inside hello"
    if name == "Todd":
        print("The hello() function has been executed!")
        return greet()
    else:
        print("The hello() function has been executed!")
        return welcome()

print(hello())
print(zz)

my_new_func = hello()
print(my_new_func)

my_second_func = hello("Dan")
print(my_second_func)
print(zz)

def cool():
    def super_cool():
        return "I am very cool"
    return super_cool()
some_func = cool()
print(some_func)
print(zz)

del hello
def hello():
    return "Hi Todd!"
def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())
other(hello)
print(zz)

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func()
def func_needs_decorator():
    print("I want to be decorated!")
func_needs_decorator()
print(zz)
new_decorator(func_needs_decorator)
print(zz)