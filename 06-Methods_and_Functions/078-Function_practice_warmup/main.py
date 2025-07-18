zz = "##########################################################"
print(zz)

print("Warmup")
print(zz)
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(3,7))
print(zz)

def animal_crackers(text):
    wordlist = text.split()
    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False
print(animal_crackers("Levelheaded Llam"))
print(animal_crackers("Crazy Kangaroo"))
print(zz)

def makes_twenty(int1,int2):
    if int1 + int2 == 20:
        return True
    elif int1 == 20 or int2 == 20:
        return True
    else:
        return False
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print(zz)