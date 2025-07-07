from matplotlib.dates import num2date

zz = "####################################################"
print(zz)

def hello():
    '''
    This function prints the word Hello
    '''
    print("Hello")

hello()
print(zz)

def hello_name(name):
    '''
    This function will print out Hello and the name that is passed in
    '''
    print("Hello "+name)

hello_name("Dan")
print(zz)

def custom_add(int1,int2):
    '''
    This function passes in two integers, adds them and returns the result
    '''
    return int1+int2
result = custom_add(1,2)
print(result)
print(zz)

