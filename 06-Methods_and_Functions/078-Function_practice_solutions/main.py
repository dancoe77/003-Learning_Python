zz = "##########################################################"
print(zz)

print("WARMUP")
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

print("Level 2 Problems")
print(zz)

def has_33(int):
    for i in range(0, len(int)-1):
        if int[i]  == 3 and int[i+1] == 3:
            return True
    return False
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
print(zz)

def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    return result
print(paper_doll("Hello"))
print(paper_doll("Mississippi"))
print(zz)

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in(a,b,c):
        return sum((a,b,c)) - 10
    else:
        return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(zz)

def summer_69(arr):
    total = 0
    add = True
    for int in arr:
        while add:
            if int != 6:
                total += int
                break
            else:
                add = False
        while not add:
            if int != 9:
                break
            else:
                add = True
                break
    return total
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))
print(zz)



