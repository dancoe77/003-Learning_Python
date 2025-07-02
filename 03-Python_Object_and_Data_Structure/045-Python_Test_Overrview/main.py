q1 = "Write a brief description of all the following Object Types and Data Structures we've learned about."
print(q1)

b = "##################################################################################################"
print(b)

q1a = "Numbers"
a1a = "Any integer or floating point unit that mathematical functions can be performed on"
print(q1a)
print(a1a)

print(b)

q1b = "Strings"
a1b = "Strings are a collection of objects that are immutable and can be called based on their index postion"
print(q1b)
print(a1b)

print(b)

q1c = "Lists"
a1c = "Lists are a collection of objects that are mutable, can be sorted and can be called based on index postion"
print(q1c)
print(a1c)

print(b)

q1d = "Tuples"
a1d = "Tuples are similar to lists except that they don't have a lot of method sets and are immutable"
print(q1d)
print(a1d)

print(b)

q1e = "Dictionaries"
a1e = "Dictionaries are similar to lists except that instead of index positions, Dictionaries employ key-value pairs"
print(q1e)
print(a1e)

print(b)

q2 = "Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25."
a2 = "n = (10 ** 2) / 2 * 4 + 1 - 100.75"
print(q2)
print(a2)
n1 = (10 ** 2) / 2 * 4 + 1 - 100.75
print(n1)

print(b)

q3a = "What is the value of the expression 4 * (6 + 5)"
a3a = "44"
print(q3a)
print(a3a)
n2 =  4 * (6 + 5)
print(n2)
print(b)
q3b = "What is the value of the expression 4 * 6 + 5"
a3b = "29"
print(q3b)
print(a3b)
n3 = 4 * 6 + 5
print(n3)
print(b)
q3c = "What is the value of the expression 4 + 6 * 5"
a3c = "34"
print(q3c)
print(a3c)
n4 = 4 + 6 * 5
print(n4)
print(b)

q4 = "What is the type of the result of the expression 3 + 1.5 + 4?"
a4 = "Floating point"
print(q4)
print(a4)
n5 = 3 + 1.5 + 4
print(n5)
print(type(n5))
print(b)

q4 = "What would you use to find a number’s square root, as well as its square?"
a4 = "n = (100 ** (1/2)) ; n = (10 ** 2)"
print(q4)
print(a4)
n6 = (100 ** (1/2))
n7 = (10 ** 2)
print(n6)
print(n7)
print(b)

q5a = "Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:"
a5a = "print(s[1])"
print(q5a)
print(a5a)
s = "hello"
print(s[1])
print(b)

q5b = "Reverse the string 'hello' using slicing:"
a5b = "print(s[-1::-1])"
print(q5b)
print(a5b)
s = "hello"
print(s[-1::-1])
print(b)

q5c = "Given the string hello, give two methods of producing the letter 'o' using indexing."
a5c = "print(s[4]) or print(s[-1])"
print(q5c)
print(a5c)
s = "hello"
print(s[4])
print(s[-1])
print(b)

q6a = "Build this list [0,0,0] two separate ways."
a6a = "I would use either concatenate or append"
print(q6a)
print(a6a)
mylist = [0,0]
print(mylist)
another_list = [0]
print(another_list)
new_list = mylist + another_list
print(new_list)
print(b)
mylist.append(0)
print(mylist)
print(b)

q7 = "Reassign 'hello' in this nested list to say 'goodbye' instead:"
a7 = "list3[-1][-1] = 'goodbye'"
print(q7)
print(a7)
list3 = [1,2,[3,4,"hello"]]
list3[-1][-1] = "goodbye"
print(list3)
print(b)

q8 = "Sort the list below:"
a8 = "list4.sort()"
print(q8)
print(a8)
list4 = [5,3,4,6,1]
print(list4)
list4.sort()
print(list4)
print(b)

q9 = "Using keys and indexing, grab the 'hello' from the following dictionaries:"
q9a = "d = {'simple_key':'hello'}"
a9a = "print(d['simple_key')"
print(q9)
print(q9a)
print(a9a)
d = {"simple_key":"hello"}
print(d["simple_key"])
print(b)

q9b = "d = {'k1':{'k2':'hello'}}"
a9b = "print(d['k1']['k2'])"
print(q9b)
print(a9b)
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
print(b)

q9c = "d = {'k1':[{'nest_key':['this is deep',['hello']]}]}"
a9c = "print(d['k1'][0]['nest_key'][1][0])"
print(q9c)
print(a9c)
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
print(b)

q9d = "d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}"
a9d = "print(d['k1'][2]['k2'][1]['tough'][2][0])"
print(q9d)
print(a9d)
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
print(b)

q10 = "Can you sort a dictionary? Why or why not?"
a10 = "Dictionaries cannot be sorted because they don't retain any order or sequence unlike lists"
print(q10)
print(a10)
print(b)

q11 = "What is the major difference between tuples and lists?"
a11 = "Tuples are immutable whereas lists are mutable"
print(q11)
print(a11)
print(b)

q12 = "How do you create a tuple?"
a12 = "t = ('one',2)"
print(q12)
print(a12)
print(b)

q13 = "What is unique about a set?"
a13 = "Sets can only contain unique items, duplicate items are removed in a set"
print(q13)
print(a13)
print(b)

q14 = "Use a set to find the unique values of the list below:"
a14 = "myset = set(list5)"
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list5)
myset = set(list5)
print(myset)
print(b)

q15 = "For the following quiz questions, we will get a preview of comparison operators"
q15a = "2 > 3"
a15a = "False"
print(q15)
print(q15a)
print(a15a)
print(2 > 3)
print(b)

q15b = "3 <= 2"
a15b = "False"
print(q15b)
print(a15b)
print(3 <= 2)
print(b)

q15c = "3 == 2.0"
a15c = "False"
print(q15c)
print(a15c)
print(3 == 2.0)
print(b)

q15d = "3.0 = 3"
a15d = "True"
print(q15d)
print(a15d)
print(3.0 == 3)
print(b)

q15e = "4**0.5 != 2"
a15e = "False"
print(q15e)
print(a15e)
print(4**0.5 != 2)
print(b)

q16 = "Final Question: What is the boolean output of the cell block below?"
a16 = "False"
print(q16)
print(a16)
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])
print(b)