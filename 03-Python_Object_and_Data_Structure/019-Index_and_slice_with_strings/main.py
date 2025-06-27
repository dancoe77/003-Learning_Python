print(len("hello"))

print(len("I am"))

mystring = "Hello World"
print(mystring)
print(mystring[0]) # H

print(mystring[8]) # r
print(mystring[-3]) # r

print(mystring[9]) # l
print(mystring[-2]) # l

print(mystring[-1]) # d

mystring = "abcdefghijk"
print(mystring)
print(mystring[2]) # c
print(mystring[2:]) # cdefghijk
print(mystring[:3]) # abc
print(mystring[3:6]) # def
print(mystring[1:3]) # bc
print(mystring[-4:-1])

print(mystring[::]) # abcdefghijk
print(mystring[::2]) # acegik
print(mystring[::3]) # adgj
print(mystring[2:7:2]) # ceg
print(mystring[::-1]) # kjihgfedcba