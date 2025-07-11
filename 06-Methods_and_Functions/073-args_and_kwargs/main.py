zz = "#######################################"
print(zz)

def sum_ints_math(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05
print(sum_ints_math(100,100))
print(zz)
print(sum_ints_math(40,60,100))
print(zz)
print(sum_ints_math(40,60,100,100))
print(zz)
print(sum_ints_math(40,60,100,100,100))
print(zz)
#print(sum_ints_math(40,60,100,100,100, 500)) this won't work

def sum_int_math_arg(*args):
    return sum(args) * 0.05
print(sum_int_math_arg(40,60))
print(zz)
print(sum_int_math_arg(40,60,100))
print(zz)
print(sum_int_math_arg(40,60,100,100))
print(zz)

def sum_int_func(*args):
    for item in args:
        print(item)
print(sum_int_func(40,60,100,100))
print(zz)

def dic_fruit_kwargs(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        return (f"My fruit of choice is {(kwargs["fruit"])}")
    else:
        pass
    return "I didn't find any fruit here"
print(dic_fruit_kwargs(fruit="apple"))
print(zz)
print(dic_fruit_kwargs(fruit="apple",veggie="lettuce"))
print(zz)
print(dic_fruit_kwargs(veggie="lettuce"))
print(zz)

def function_arg_kwarg(*args,**kwargs):
    return (f"I would like {args[0]} {(kwargs["food"])}")
print(function_arg_kwarg(10,20,30,fruit="orange",food="eggs",animal="dog"))
print(zz)

