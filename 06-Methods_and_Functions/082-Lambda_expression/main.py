zz = "##########################################################"
print(zz)

def square(int):
    return int**2

ints = [0,1,2,3,4]
print(map(square,ints))
for value in map(square,ints):
    print(value)
print(zz)
print(list(map(square,ints)))
print(zz)

def splicer(string):
    if len(string)%2 == 0:
        return "EVEN"
    else:
        return string[0]
names = ["Andy","Eve","Sally"]
print(list(map(splicer,names)))
print(zz)

def check_even(int):
    if int%2 == 0:
        return True
    else:
        return False
ints = [0,1,2,3,4,5]
print(map(check_even,ints))
for value in map(check_even,ints):
    print(value)
print(zz)
print(list(map(check_even,ints)))
print(zz)
print(filter(check_even,ints))
print(zz)
print(list(filter(check_even,ints)))
print(zz)
for v in filter(check_even,ints):
    print(v)
print(zz)

def square(int):
    result = int ** 2
    return result
print(square(3))
print(zz)
square = lambda int:int ** 2
print(square(3))
print(zz)
print(square(5))
print(zz)

print(list(map(lambda int:int**2,ints)))
print(zz)

print(list(filter(lambda int:int%2 == 0,ints)))
print(zz)

print(list(map(lambda name:name[0],names)))
print(zz)

print(list(map(lambda name:name[::-1],names)))
print(zz)