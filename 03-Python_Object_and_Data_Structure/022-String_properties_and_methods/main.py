name = "Sam"
print(name)
# name[0] = "P" doesn't work

print(name[1:]) # am

last_letters = name[1:]
print(last_letters)

print("P" + last_letters) # Pam

x = "Hello World"
y = " it is beautiful outside!"
print(x + y) # Hello World it is beautiful outside!

letter = "z"
print(letter * 10) # zzzzzzzzzz

print(2 + 3) # 5
print("2" + "3") # 23

x = "Hello World"
print(x.upper()) # HELLO WORLD
print(x.upper) # function str.upper
print(x.lower()) # hello world
print(x.split()) # ['Hello', 'World']

x = "Hello Nebula"
print(x)
print(x.split("e")) # ['H', 'llo N', 'bula']