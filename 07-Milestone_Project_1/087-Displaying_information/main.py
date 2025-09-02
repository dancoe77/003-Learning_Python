zz = "##################################################"
print(zz)

print([1,2,3])
print(zz)

print([1,2,3])
print([4,5,6])
print([7,8,9])
print(zz)

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

example_row = [1,2,3]

display(example_row, example_row, example_row)
print(zz)

#row1 = [1,2,3]
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display(row1,row2,row3)
print(zz)

row2[1] = "X"
display(row1, row2, row3)
print(zz)