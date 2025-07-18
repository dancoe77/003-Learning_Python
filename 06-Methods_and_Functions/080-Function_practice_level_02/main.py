zz = "##########################################################"
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