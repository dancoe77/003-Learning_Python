zz = "##########################################################"
print(zz)

print("Lvl 1 Problems")
print(zz)

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short!"
print(old_macdonald("macdonald"))
print(zz)

def master_yoda(text):
    s = (text.split()[::-1])
    delimiter = " "
    result = delimiter.join(s)
    return result
print(master_yoda("I am home"))
print(master_yoda("We are ready"))
print(zz)

def almost_there(int):
    if abs(100 - int) <=10:
        return True
    elif abs(200 - int) <=10:
        return True
    else:
        return False
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(200))
print(zz)