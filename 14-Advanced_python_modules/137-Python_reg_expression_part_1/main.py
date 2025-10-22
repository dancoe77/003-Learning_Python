zz = "###########################################"
print(zz)

print("dog" in "my dog is great")
print(zz)

print("user@email.com")
print("'text' + '@' + 'text' + '.com'")
print(zz)

print("(555)-555-5555")
print("r'(\d\d\d)-\d\d\d-\d\d\d\d'")
print("r'(\d{3})-\d{3}-\d{4}'")
print(zz)

text = "The agent's phone number is 408-555-1234. Call soon!"
print(text)
print("phone" in text)
print(zz)

import re
pattern = "phone"
print(re.search(pattern, text))
print(zz)

pattern = "NOT IN TEXT"
print(re.search(pattern, text))
print(zz)

pattern = "phone"
match = re.search(pattern, text)
print(match)
print(zz)
print(match.span())
print(match.start())
print(match.end())
print(zz)

text = "my phone once, my phone twice"
print(text)
match = re.search("phone", text)
print(match)
print(zz)

matches = re.findall("phone", text)
print(matches)
print(len(matches))
print(zz)

for match in re.finditer("phone", text):
    print(match.group())
print(zz)