zz = "##########################################"
print(zz)

mylist = [1,2,3]
print(mylist)
print(len(mylist))
print(zz)

class Sample():
    pass
mysample = Sample()
print(mysample)
#print(len(mysample()))
print(type(mysample))
print(zz)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} has {self.pages} pages."
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")
bb = Book("Golang Rocks!!", "Todd McLeod",200)
print(bb)
print(len(bb))
del(bb)
# print(bb)
print(zz)