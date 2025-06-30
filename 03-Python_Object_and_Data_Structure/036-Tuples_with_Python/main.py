t = (1,2,3)
mylist = [1,2,3]
print(t)
print(type(t))
print(mylist)
print(type(mylist))

b = "#########################################"
print(b)

print(len(t))
print(len(mylist))

print(b)

t = ("one",2)
print(t[0])
print(t[-1])

print(b)

t = ("a","a","b")
print(t)
print(t.count("a"))
print(t.index("a"))
print(t.index("b"))

print(b)

print(t)
print(mylist)

mylist[0] = "NEW"
print(mylist)
# t[0] = "NEW" won't work because tuples are immutable