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

print(input("Please enter a value: "))
print(zz)

result = input("Please enter a value: ")
print(result)
print(type(result))
print(zz)

result = input("Please enter a value: ")
print(type(result))
result_int = int(result)
print(type(result_int))
print(zz)

print(2.3)
print(type(2.3))

print("3.14")
print(type("3.14"))
result_float = float("3.14")
print(type(result_float))
print(zz)

position_index = input("Choose an index position: ")
print(position_index)
print(type(position_index))
print(zz)

position_index = int(input("Choose an index position: "))
print(position_index)
print(type(position_index))
print(zz)

print(row2[position_index])
print(zz)