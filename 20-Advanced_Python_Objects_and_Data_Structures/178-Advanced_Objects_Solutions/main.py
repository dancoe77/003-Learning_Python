zz = "#################################################################"
print(zz)

aa = "Problem 1: Convert 1024 to binary and hex"
print(aa)
print(bin(1024))
print(hex(1024))
print(zz)

bb = "Problem 2: Round 5.23222 to two decimal places"
print(bb)
i = 5.23222
print(round(i,2))
print(zz)

cc = "Problem 3: Check if every letter in the string s is lower case"
print(cc)
s = "hello how are you Mary, are you feeling okay?"
print(s)
print(s.islower())
print(zz)

dd = "Problem 4: How many times does the letter 'w' show up in the string below?"
print(dd)
t = "twywywtwywbwhsjhwuwshshwuwwwjdjdid"
print(t)
print(t.count("w"))
print(zz)

ee = "Problem 5: Find the elements in set1 that are not in set2"
print(ee)
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1)
print(set2)
print(set1.difference(set2))
print(zz)

ff = "Problem 6: Find all the elements that are in either set"
print(ff)
print(set1.union(set2))
print(zz)

gg = "Problem 7: Create this dictionary: {0:0, 1:1, 2:8, 3:27, 4:64}"
print(gg)
print({x:x**3 for x in range(5)})
print(zz)

hh = "Problem 8: Reverse the list below:"
print(hh)
l = [1,2,3,4]
print(l)
l.reverse()
print(l)
print(zz)

ii = "Problem 9: Sort the list below:"
print(ii)
m = [3,4,2,5,1]
print(m)
m.sort()
print(m)
print(zz)