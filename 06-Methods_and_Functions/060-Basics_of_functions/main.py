zz = "#######################################"
print(zz)

def say_hello():
    print("hello")
    print("are")
    print("you")
say_hello()
print(zz)

def say_hello(name="Colista"):
    print(f'Hello {name}')
say_hello("Dan")
say_hello()
print(zz)

def add_int(int1,int2):
    return int1 + int2
result = add_int(10,20)
print(result)
print(zz)

def print_result(a,b):
    print(a+b)
def return_result(a,b):
    return a + b
result = print_result(10,20)
print(type(result))
print(zz)

result = return_result(10,20)
print(result)
print(type(result))
print(zz)

def myfunc(a,b):
    print(a + b)
    return a + b
result = myfunc(10, 20)
print(zz)

def sum_ints(int1,int2):
    return int1 + int2
intresult = sum_ints(10,20)
print(intresult)
print(type(intresult))
print(zz)

stringresult = sum_ints("10","20")
print(stringresult)
print(type(stringresult))
print(zz)
