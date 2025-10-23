zz = "####################################################"
print(zz)

import re
print(re.search(r"cat","The cat is here"))
print(zz)
print(re.search(r"cat|dog","The dog is here"))
print(zz)

print(re.findall(r"at","The cat in the hat sat there."))
print(zz)
print(re.findall(r".at","The cat in the hat sat there."))
print(zz)
print(re.findall(r"...at","The cat in the hat went splat."))
print(zz)

print(re.findall(r"^\d","1 is a number"))
print(zz)
print(re.findall(r"\d$","The number is 2"))
print(zz)

phrase = "There are 3 numbers 34 inside 5 this sentence"
pattern = r"[^\d]+"
print(re.findall(pattern,phrase))
print(zz)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
test_pattern = r"[^!.? ]+"
print(re.findall(test_pattern,test_phrase))
print(zz)
clean = re.findall(test_pattern,test_phrase)
print(" ".join(clean))
print(zz)

text = "Only find the hypen-words  in this sentence. But you do not know how long-ish they are"
pattern = r"[\w]+"
print(re.findall(pattern,text))
print(zz)
pattern = r"[\w]+-[\w]+"
print(re.findall(pattern,text))
print(zz)

text = "Hello, would you like some catfish?"
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
print(re.search(r"cat(fish|nap|claw)",text))
print(re.search(r"cat(fish|nap|claw)",texttwo))
print(re.search(r"cat(fish|nap|erpillar)",textthree))
print(zz)
print(re.search(r"cat[\D]*[^?]",text))
print(re.search(r"cat[\D]*[^?]",texttwo))
print(re.search(r"cat[\D]*[^?]",textthree))
print(zz)
