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

print("Challenging Problems")
print(zz)

def spy_game(ints):
    code = [0,0,7,"v"]

    for int in ints:
        if int == code[0]:
            code.pop(0)
    return len(code) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(zz)

def count_primes(int):
    primes = [2]
    v = 3
    if int < 2:
        return 0
    while v <= int:
        for w in primes:
            if v%w == 0:
                v += 2
                break
        else:
            primes.append(v)
            v += 2
    print(primes)
    return len(primes)
print(count_primes(100))
print(zz)

def print_big(string):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[string.upper()]:
        print(patterns[pattern])
print_big("a")
print(zz)