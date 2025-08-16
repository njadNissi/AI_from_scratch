# # functions declarations

# func_list1 = []
# for i in range(5):
#     def func(e):
#         return e+i # will use late binding. the last value of i in the code
#     func_list1.append(func)


# func_list2 = []
# for i in range(5):
#     def func(e, iv=i):
#         return e+iv # will use early binding, a constant value of iv as defined in the function
#     func_list2.append(func)


# func_list3 = [lambda e:e+i for i in range(5)]
# func_list4 = [lambda e, iv=i: e+iv for i in range(5)]  


# i = 56

# print([f(10) for f in func_list1])
# print([f(10) for f in func_list2])
# print([f(10) for f in func_list3])
# print([f(10) for f in func_list4])




# a verison of the built-in range functions, with 2 or 3 args(and positive steps) can be implemented as:

def myrange(start, stop=0, step=1):
    """
        enumerates the values from start in steps of size step that are less than stop
    """

    assert step > 0, "only positive steps implemented in myrange"
    i = start
    if stop == 0:
        i = 0
        stop = start # if only one arg, the the passed arg is the stop. and start=0
    while i < stop:
        yield i # the yield cmd returns a value that is  obtained with next
        i += step

print('first=', next(myrange(30)), "; list(myrange(30):", list(myrange(30)))
print("list(myrange(2, 30, 3):", list(myrange(2, 30, 3)))




def squares(x):
    """generated the square of even nonnegative integers less than x"""
    for e in range(x):
        yield e*e
    
a = squares(20)
print('SQUARE=', next(a), next(a), next(a))



# a version of enumerate 

def myenum(enum):
    for i in range(len(enum)):
        yield i, enum[i] # tupe（index, value）

a = [1, 4, 6]
b = myenum(a)
print(next(b))
print(next(b))