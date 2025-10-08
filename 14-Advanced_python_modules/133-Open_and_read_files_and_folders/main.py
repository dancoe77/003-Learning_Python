zz = "##################################################"
print(zz)

import os
def working_directory():
    return os.getcwd()
print(working_directory())
print(zz)

f = open("practice.txt","w+")
f.write("this is a test string")
f.close()

print(os.listdir())
print(zz)

print(os.listdir("/home/dan"))
print(zz)

import shutil
# shutil.move("practice.txt","/home/dan/Class/003-Learning_Python/14-Advanced_python_modules")
print(os.listdir("/home/dan/Class/003-Learning_Python/14-Advanced_python_modules"))
print(zz)

import send2trash

# send2trash.send2trash("practice.txt")

file_path ="/home/dan/Class/003-Learning_Python/14-Advanced_python_modules"
for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"File: {f}")
    print("\n")
print(zz)