zz = "####################################"
print(zz)

print("Use for, .split(), and if to create a Statement that will print out words that start with 's':")
st = "Print only the words that start with s in this sentence"
st_split = st.split()
for letter in st_split:
    if letter[0] == "s":
        print(letter)
print(zz)

print("Use range() to print all the even numbers from 0 to 10.")
print(list(range(0,11,2)))
print(zz)

print("Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.")
int = [int for int in range(1,51) if int%3 == 0]
print(int)
print(zz)

print("Go through the string below and if the length of a word is even print 'even!'")
st = "Print every word in this sentence that has an even number of letters"
st_split = st.split()
for letter in st_split:
    if len(letter)%2 == 0:
        print(letter," even")
print(zz)

print("Write a program that prints the integers from 1 to 100.")
print("But for multiples of three print 'Fizz' instead of the number, and for the multiples of five print 'Buzz'.")
print("For numbers which are multiples of both three and five print 'FizzBuzz'")
for int in range(1,101):
    if int%15 == 0:
        print("FizzBuzz")
    elif int%5 == 0:
        print("Buzz")
    elif int%3 == 0:
        print("Fizz")
    else:
        print(int)
print(zz)

print("Use List Comprehension to create a list of the first letters of every word in the string below:")
st = 'Create a list of the first letters of every word in this string'
mystring = [letter[0] for letter in st.split()]
print(mystring)
print(zz)