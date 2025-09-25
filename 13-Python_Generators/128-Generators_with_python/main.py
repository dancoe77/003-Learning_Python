zz = "####################################################"
print(zz)

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
print(create_cubes(10))
print(zz)

for x in create_cubes(10):
    print(x)
print(zz)
del create_cubes

def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3
print(create_cubes(10))
print(zz)

for x in create_cubes(10):
    print(x)
print(zz)

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in gen_fibon(10):
    print(num)
print(zz)

def simple_gen():
    for i in range(3):
        yield i
for num in simple_gen():
    print(num)
print(zz)
g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
print(zz)

s = "hello"
for letter in s:
    print(letter)
# next(s)
print(zz)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(zz)