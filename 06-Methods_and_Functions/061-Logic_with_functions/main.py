zz = "################################################"
print(zz)

print(2 % 2)
print(zz)

print(3 % 2)
print(zz)

print(41 % 40)
print(zz)

print(20 % 2)
print(zz)

print(20 % 2 == 0)
print(zz)

print(21 % 2 == 0)
print(zz)

def even_check(int):
    result = int % 2 == 0
    return result
print(even_check(20))
print(zz)

print(even_check(21))
print(zz)

# Return true if any number is even inside a list
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1,3,5,7,9]))
print(zz)
print(check_even_list([0,2,4,6,8]))
print(zz)


def check_even_list_expanded(num_list):

    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(check_even_list_expanded([2,1,1,1]))
print(zz)
print(check_even_list_expanded([1,1,1,2]))
print(zz)
print(check_even_list_expanded([0,2,4,6,8]))
print(zz)