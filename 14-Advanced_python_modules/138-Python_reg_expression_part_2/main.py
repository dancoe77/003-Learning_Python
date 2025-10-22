zz = "####################################################"
print(zz)

import re
text = "My phone number is 408-555-1234"
phone = re.search("408-555-1234", text)
print(phone)
print(zz)

phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(phone)
print(phone.group())
print(zz)

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
print(zz)