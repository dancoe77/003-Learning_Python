f = open("myfile.txt","w", encoding="utf-8")
f.write("Hello this is a text file\n")
f.write("This is the second line\n")
f.write("This is the third line\n")
f.close()

myfile = open("myfile.txt")
print(myfile)
myfile.close()

b = "############################################"
print(b)

# myfile = open("whoops_wrong.txt") # no such file

from pathlib import Path
print(Path.cwd())

print(b)

myfile = open("myfile.txt")
print(myfile.read())
myfile.close()
print(b)
myfile = open("myfile.txt")
print(myfile.read())
#myfile.seek(0) - returns the cursor to the top of the line
myfile.close()
print(b)
myfile = open("myfile.txt")
print(myfile.readlines())
myfile.close()
print(b)
# myfile = open("/Users/YourUserName/Folder/myfile.txt")
with open("myfile.txt") as  my_new_file:
    contents = my_new_file.read()
    print(contents)
    print(b)
with open("myfile.txt","r") as myfile:
    contents = myfile.read()
    print(contents)
    print(b)

f = open("my_new_file.txt","w", encoding="utf-8")
f.write("ONE ON FIRST\n")
f.write("TWO ON SECOND\n")
f.write("THREE ON THIRD\n")
f.close()
print(f)

print(b)

with open("my_new_file.txt","r") as f:
    print(f.read())
    print(b)
with open("my_new_file.txt","a") as f:
    f.write("FOUR ON FOURTH\n")
with open("my_new_file.txt","r") as f:
    print(f.read())
    print(b)