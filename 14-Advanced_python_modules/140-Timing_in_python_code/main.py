zz = "#################################################"
print(zz)

print(10)
print(3)
print(["1","2","3"])
print(zz)

def func_one(i):
    return [str(num) for num in range(i)]
print(func_one(10))
print(zz)

def func_two(i):
    return list(map(str, range(i)))
print(func_two(10))
print(zz)

import time
start_time = time.time()
result = func_one(10)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
print(zz)

start_time = time.time()
result = func_two(10)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
print(zz)

import timeit
stmt = '''
func_one(100)
'''
setup = '''
def func_one(i):
    return [str(num) for num in range(i)]
'''
print(timeit.timeit(stmt, setup=setup, number=100000))
print(zz)

stmt = '''
func_two(100)
'''
setup = '''
def func_two(i):
    return list(map(str, range(i)))
'''
print(timeit.timeit(stmt, setup=setup, number=100000))
print(zz)