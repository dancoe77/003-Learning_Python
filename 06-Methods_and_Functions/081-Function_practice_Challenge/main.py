zz = "##########################################################"
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