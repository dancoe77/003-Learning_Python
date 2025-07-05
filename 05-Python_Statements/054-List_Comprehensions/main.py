zz = "###################################"
print(zz)

mystring = "Hello"
mylist = []
print(mylist)
for letter in mystring:
    mylist.append(letter)
print(mylist)
print(zz)

mylist = [letter for letter in mystring]
print(mylist)
print(zz)

mylist = [x for x in "word"]
print(mylist)
print(zz)

mylist = [qweqwe for qweqwe in "wordtwo"]
print(mylist)
print(zz)

mylist = [num for num in range(0,10)]
print(mylist)
print(zz)

mylist = [num**2 for num in range(0,10)]
print(mylist)
print(zz)

mylist = [num for num in range(0,10) if num%2 == 0]
print(mylist)
print(zz)

mylist = [num**2 for num in range(0,10) if num%2 == 0]
print(mylist)
print(zz)

celcius = [0,10,20,30,40,50]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
print(zz)

results = [x if x%2==0 else "ODD" for x in range(0,10)]
print(results)
print(zz)

mylist = []

for x in [0,2,4,6,8]:
    for y in [1,3,5,7,9]:
        mylist.append(x*y)
print(mylist)
print(zz)

mylist = [x*y for x in [0,2,4,6,8] for y in [1,3,5,7,9]]
print(mylist)
print(zz)