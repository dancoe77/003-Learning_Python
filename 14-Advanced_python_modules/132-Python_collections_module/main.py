zz = "#################################"
print(zz)

from collections import Counter
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
print(Counter(my_list))
print(zz)

mylist = ["a","a",10,10,10]
print(Counter(mylist))
print(zz)

print(Counter("aaaabbbbshshsjs"))
print(zz)

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))
print(zz)

letters = "aaabbbbccccccccddddddddddd"
c = Counter(letters)
print(c)
print(zz)

print(c.most_common())
print(c.most_common(2))
print(c.most_common(3))
print(zz)

print(list(c))
print(zz)

from collections import defaultdict
d = {"a":10}
print(d)
print(d["a"])
print(zz)

d = defaultdict(lambda: 0)
d["correct"] = 100
print(d["correct"])
print(zz)

print(d["wrong key"])
print(zz)

print(type(d))
print(d)
print(zz)

mytuple = (10,20,30)
print(mytuple)
print(type(mytuple))
print(mytuple[0])
print(zz)

from collections import namedtuple
dog = namedtuple("Dog",["age","breed","name"])
sammy = dog(age=5, breed="Husky", name="Sam")
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])
print(zz)