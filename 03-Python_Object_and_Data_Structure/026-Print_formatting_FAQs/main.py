print("I imported print from the __future__ module, now print isn't working. What happened?")
print("This is because once you import from the __future__ module in Python 2.7, a print statement will no longer work, and print must then use a print() function")
print("Meaning that you must use print('Whatever you were going to print') or if you are using some formatting: print('This is a string with an {p}'.format(p='insert'))")
print("The __future__ module allows you to use Python3 functionality in a Python2 environment, but some functionality is overwritten (such as the print statement, or classic division when you import division).")
print("Since we are using Jupyter Notebooks, once you so the import, all cells will require the use if the print() function. You will have to restart Python or start a new notebook to regain the old functionality back.")
