s = set()
s.add(1)
s.add(2)
print(s)
s.add(2)
print(s)
s.clear()
print(s)
t = {1, 2, 3}
u = t.copy()
print(u)
t.add(4)
print(t)
print(u)
print(t.difference(u))
v = {1, 2, 3}
w = {1, 4, 5}
v.difference_update(w)
print(v)
t.discard(2)
print(t)
v = {1, 2, 3}
w = {1, 2, 4}
print(v.intersection(w))
v.intersection_update(w)
print(v)
x = {1, 2}
y = {1,2,4}
z = {5}
print(x.isdisjoint(y))
print(x.isdisjoint(z))
print(x.issubset(y))
print(y.issuperset(x))
print(x.symmetric_difference(y))
print(x.union(y))
# x.update(y)
# print(x)