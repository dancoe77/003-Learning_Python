zz = "#########################################################"
yy = "---------------------------------------------------------"
print(zz)

aa = "WARMUP SECTION"
bb = "LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd"
bb1 = "lesser_of_two_evens(2,4) --> 2"
bb2 = "lesser_of_two_evens(2,5) --> 5"
cc = "ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter"
cc1 = "animal_crackers('Levelheaded Llama') --> True"
cc2 = "animal_crackers('Crazy Kangaroo') --> False"
dd = "MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False"
dd1 = "makes_twenty(20,10) --> True"
dd2 = "makes_twenty(2,3) --> False"
print(aa)
print(yy)
print(bb)
print(bb1)
print(bb2)
print(yy)
print(cc)
print(cc1)
print(cc2)
print(yy)
print(dd)
print(dd1)
print(dd2)
print(zz)

aa = "LEVEL 1 PROBLEMS"
bb = "OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name"
bb1 = "old_macdonald('macdonald') --> MacDonald"
bb2 = "Note: 'macdonald'.capitalize() returns 'Macdonald'"
cc = "MASTER YODA: Given a sentence, return a sentence with the words reversed"
cc1 = "master_yoda('I am home') --> 'home am I'"
cc2 = "master_yoda('We are ready') --> 'ready are We'"
cc3 = "Note: The .join() method may be useful here."
cc4 = "The .join() method allows you to join together strings in a list with some connector string."
cc5 = "For example, some uses of the .join() method:"
cc6 = ">>> '--'.join(['a','b','c'])"
cc7 = ">>> 'a--b--c'"
cc8 = "This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:"
cc9 = ">>> " ".join(['Hello','world'])"
cc10 = ">>> 'Hello world'"
dd = "ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200"
dd1 = "almost_there(90) --> True"
dd2 = "almost_there(104) --> True"
dd3 = "almost_there(150) --> False"
dd4 = "almost_there(209) --> True"
dd5 = "NOTE: abs(num) returns the absolute value of a number"
print(aa)
print(yy)
print(bb)
print(bb1)
print(bb2)
print(yy)
print(cc)
print(cc1)
print(cc2)
print(cc3)
print(cc4)
print(cc5)
print(cc6)
print(cc7)
print(cc8)
print(cc9)
print(cc10)
print(yy)
print(dd)
print(dd1)
print(dd2)
print(dd3)
print(dd4)
print(dd5)
print(zz)

aa = "LEVEL 2 PROBLEMS"
bb = "FIND 33:"
bb1 = "Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."
bb2 = "has_33([1, 3, 3]) → True"
bb3 = "has_33([1, 3, 1, 3]) → False"
bb4 = "has_33([3, 1, 3]) → False"
cc = "PAPER DOLL: Given a string, return a string where for every character in the original there are three characters"
cc1 = "paper_doll('Hello') --> 'HHHeeellllllooo'"
cc2 = "paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"
dd = "BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum."
dd1 = "If their sum exceeds 21 and there's an eleven, reduce the total sum by 10."
dd2 = "Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'"
dd3 = "blackjack(5,6,7) --> 18"
dd4 = "blackjack(9,9,9) --> 'BUST'"
dd5 = "blackjack(9,9,11) --> 19"
ee = "SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9)."
ee1 = "Return 0 for no numbers."
ee2 = "summer_69([1, 3, 5]) --> 9"
ee3 = "summer_69([4, 5, 6, 7, 8, 9]) --> 9"
ee4 = "summer_69([2, 1, 6, 9, 11]) --> 14"
print(aa)
print(yy)
print(bb)
print(bb1)
print(bb2)
print(bb3)
print(bb4)
print(yy)
print(cc)
print(cc1)
print(cc2)
print(yy)
print(dd)
print(dd1)
print(dd2)
print(yy)
print(dd3)
print(dd4)
print(dd5)
print(yy)
print(ee)
print(ee1)
print(yy)
print(ee2)
print(ee3)
print(ee4)
print(zz)

aa = "CHALLENGING PROBLEMS"
bb = "SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order"
bb1 = "spy_game([1,2,4,0,0,7,5]) --> True"
bb2 = "spy_game([1,0,2,4,0,5,7]) --> True"
bb3 = "spy_game([1,7,2,0,4,5,0]) --> False"
cc = "COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number"
cc1 = "count_primes(100) --> 25"
cc2 = "By convention, 0 and 1 are not prime."
dd = "Just for fun:"
dd1 = "PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter"
dd2 = "print_big('a')"
dd3 = "out:   * "
dd4 = "      * *"
dd5 = "     *****"
dd6 = "     *   *"
dd7 = "     *   *"
dd8 = "HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns."
dd9 = "For purposes of this exercise, it's ok if your dictionary stops at 'E'."
print(aa)
print(yy)
print(bb)
print(bb1)
print(bb2)
print(bb3)
print(yy)
print(cc)
print(cc1)
print(cc2)
print(yy)
print(dd)
print(dd1)
print(yy)
print(dd2)
print(dd3)
print(dd4)
print(dd5)
print(dd6)
print(dd7)
print(dd8)
print(dd9)
print(zz)