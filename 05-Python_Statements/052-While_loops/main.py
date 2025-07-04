zz = "#########################################"
print(zz)
x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
print(zz)

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("X IS NOT LESS THAN 5")
print(zz)

x = [0,1,2]
for item in x:
    # comment
    pass
print("end of my script")
print(zz)

mystring = "Sammy"
for letter in mystring:
    print(letter)
print(zz)

for letter in mystring:
    if letter == "a":
        continue
    print(letter)
print(zz)

for letter in mystring:
    if letter == "m":
        break
    print(letter)
print(zz)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print(zz)