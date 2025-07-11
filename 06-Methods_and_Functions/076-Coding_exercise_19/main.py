zz = "#################################"
print(zz)

def change_case(mystring):
    new_string = ''
    for index in range(len(mystring)):
        if index%2 == 0:
            new_string += mystring[index].lower()
        else:
            new_string += mystring[index].upper()
    return new_string
print(change_case("Beetlejuice"))
print(zz)