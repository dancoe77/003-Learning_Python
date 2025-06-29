my_dict = {"key1":"value1","key2":"value2"}
print(my_dict)
print(my_dict["key1"])

b = "################################################"
print(b)

prices_lookup = {"apple":2.99,"orange":1.99,"milk":5.80}
print(prices_lookup["apple"])

print(b)

d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
print(d["k2"])
print(d["k3"]["insideKey"])
print(d["k2"][2])

print(b)

d = {"key1":["a","b","c"]}
print(d)
print(d["key1"][2])
mylist = d["key1"]
letter = mylist[2]
print(letter.upper())
print(d["key1"][2].upper())

print(b)

d = {"k1":100,"k2":200}
print(d)
d["k3"] = 300
print(d)
d["k1"] = "NEW"
print(d)
d["k1"] = 100
print(d)
print(d.keys())
print(d.values())
print(d.items())