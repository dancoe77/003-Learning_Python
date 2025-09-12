zz = "##########################################################"
print(zz)

aa = "Problem 1"
bb = "Handle the exception thrown by the code below by using try and except blocks"
print(aa)
print(bb)
print(zz)

try:
    for i in ["a","b","c"]:
        print(i**2)
except:
    print("General error! Watch out!")
print(zz)

cc = "Problem 2"
dd = "Handle the exception thrown by the code by using try and except blocks"
ee = "Then use a finally block to print 'All Done'"
print(cc)
print(dd)
print(ee)
print(zz)

try:
    x = 5
    y = 0
    z = x/y
except:
    print("Error!")
finally:
    print("All Done")
print(zz)

ff = "Problem 3"
gg = "Write a function that asks for an integer and prints the square of it"
hh = "Use a while loop with a try, except, else block to account for incorrect inputs"
print(ff)
print(gg)
print(hh)
print(zz)

def ask():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please enter an number! \n")
            continue
        else:
            result = n**2
            print("Your number squared is: ")
            print(result)
            break
ask()
print(zz)