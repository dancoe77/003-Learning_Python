zz = "######################################################"
print(zz)

def vol(rad):
    import math
    return (4/3) * math.pi * (rad)**3
print(vol(2))
print(zz)

def ran_check(int,low,high):
    if int <= high and int >= low:
        return print(f"{int} is in the range between {low} and {high}")
    else:
        return print(f"{int} is not in the range between {low} and {high}")
ran_check(5,2,7)
ran_check(0,2,7)
print(zz)

def ran_bool(int,low,high):
    if int <= high and int >= low:
        return True
    else:
        return False
print(ran_bool(3,1,10))
print(zz)

def up_low(s):
    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
print(zz)

def unique_list(lst):
    lst_set = set(lst)
    return lst_set
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print(zz)

def multiply(ints):
    total = 1
    for v in ints:
        total *= v
    return total
print(multiply([1,2,3,-4]))
print(zz)

def palindrome(s):
    s = s.replace(" ","")
    if s == s[::-1]:
        return True
    else:
        return False
print(palindrome("nurses run"))
print(palindrome("abcba"))
print(zz)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)

    str1 = str1.replace(" ","")
    str1 = str1.lower()
    str1 = set(str1)
    if str1 == alphaset:
        return True
    else:
        return False
print(ispangram("The quick brown fox jumps over the lazy dog"))
print(string.ascii_lowercase)
print(zz)