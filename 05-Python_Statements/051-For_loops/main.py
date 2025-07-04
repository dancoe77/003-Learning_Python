z = "###################################"
print(z)
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
print(z)

for jelly in mylist:
    print(jelly)
print(z)

for jelly in mylist:
    print("hello")
print(z)

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
print(z)

for num in mylist:
    # Check for odd
    if num % 2 != 0:
        print(num)
print(z)

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")
print(z)

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)
print(z)

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)
print(z)

mystring = "Hello Milky Way"
for letter in mystring:
    print(letter)
print(z)

tup = (1,2,3,4,5)
for item in tup:
    print(item)
print(z)

mylist = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(len(mylist))
for item in mylist:
    print(item)
print(z)

for (a,b) in mylist:
    print(a)
    print(b)
print(z)

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for item in mylist:
    print(item)
print(z)

mylist = [(0,1,2),(3,4,5),(6,7,8)]
for (a,b,c) in mylist:
    print(a)
    print(b)
    print(c)
print(z)

d = {"k1":0,"k2":1,"k3":2}
for item in d:
    print(item)
print(z)

for item in d.items():
    print(item)
print(z)

for key,value in d.items():
    print(key)
    print(value)
print(z)

for value in d.values():
    print(value)
print(z)