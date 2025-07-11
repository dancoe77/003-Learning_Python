zz = "#########################################"
print(zz)

def pick_evens(*args):
    list_even = []
    for num in args:
        if num%2 == 0:
            list_even.append(num)
    else:
        pass
    return list_even
print(pick_evens(0,3,5,2,4,7))
print(zz)