zz = "#######################################"
print(zz)
mylist = [0,1,2]
for num in range(10):
    print(num)
print(zz)

for num in range(3,10):
    print(num)
print(zz)

for num in range(0,10,2):
    print(num)
print(zz)

print(range(0,10,2))
print(zz)

print(list(range(0,10,2)))
print(zz)

index_count = 0
for letter in "abcde":
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1
print(zz)

index_count = 0
word = "abcde"
for letter in word:
    print(word[index_count])
    index_count += 1
print(zz)

word = "abcde"
for item in enumerate(word):
    print(item)
print(zz)

word = "abcde"
for index,letter in enumerate(word):
    print(index)
    print(letter)
    #print("\n")
print(zz)

mylist1 = [0,1,2,3,4]
mylist2 = ["a","b","c","d","e"]
for item in zip(mylist1,mylist2):
    print(item)
print(zz)

mylist1 = [0,1,2,3,4]
mylist2 = ["a","b","c","d","e"]
mylist3 = [100,200,300,400,500]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
print(zz)
print(list(zip(mylist1,mylist2,mylist3)))
print(zz)

print("x" in [1,2,3])
print(zz)

print("x" in ["x","y","z"])
print(zz)

print("a" in "a world")
print(zz)

print("mykey" in {"mykey":0})
print(zz)

d = {"mykey":0}
print(0 in d.values())
print(zz)

d = {"mykey":0}
print(0 in d.keys())
print(zz)

mylist = [10,20,30,40,50]
print(min(mylist))
print(zz)

print(max(mylist))
print(zz)

from random import shuffle
mylist = [0,1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)
print(zz)
shuffle(mylist)
print(mylist)
print(zz)

from random import randint
print(randint(0,100))
print(zz)

mynum = randint(0,100)
print(mynum)
print(zz)

user_input = input("Enter a number here: ")
print(user_input)
print(type(user_input))
print(zz)

user_float = float(user_input)
print(user_float)
print(type(user_float))
print(zz)