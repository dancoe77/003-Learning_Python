zz = "##########################################"
print(zz)

def add(n1,n2):
    print(n1+n2)
add(10,20)
print(zz)

number1 = 10
number2 = 20
#number2 = int(input("Please provide a number: "))
add(number1,number2)
print("Something happened!")
print(zz)

try:
    # Want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print("Hey it looks like you are not adding correctly")
else:
    print("Add went well")
    print(result)
print(zz)

try:
    f = open("testfile","w")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
except:
    print("All other exceptions")
finally:
    print("I always run")
print(zz)

def ask_for_int():
    while True:
        try:
            result = int(input("Please privide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes, thank you")
            print(result)
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")
ask_for_int()
print(zz)