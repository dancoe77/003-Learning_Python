zz = "###############################################"
print(zz)

def gensquares(N):
    for i in range(N):
        yield i**2
for x in gensquares(10):
    print(x)
print(zz)

import random
random.randint(1,10)

def ran_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for num in ran_num(1,10,12):
    print(num)
print(zz)

s = "hello"
s = iter(s)
print(next(s))
print(zz)
aa = "Explain a use case for a generator using a yield statement where we would not want to use a normal function with a return statement"
bb = "If the ouput has the potential of taking up a large amount of memory and we only intend to iterate through, use a generator"
print(aa)
print(bb)
print(zz)

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
cc = "instead of list comprehension change [] to () and we now have a generator to iterate through the list"
print(cc)
print(zz)