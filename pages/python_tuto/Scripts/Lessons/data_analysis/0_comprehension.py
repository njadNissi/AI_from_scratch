#(fe for e in iter if cond): enumerate the values 'fe' for each 'e' in 'iter' for which 'cond' is true.
# comprehension work for list, tuple, set and dics.



# list = [e*e for e in range(20) if e%2==0]
# print(list)
# tuple = (e*e for e in range(20) if e %2==0)
# a = next(tuple)
# b = next(tuple)
# print(a, b,  tuple)


# dictionary comprehension

# keys = ["a", "f", "bar", "b", "a", "aaaaa"]
# dic1 = {keys[i]:i for i in range(len(keys))}
# dic2 = {val:i for (i, val) in enumerate(keys)}
# print(dic1, 'key=b => val=', dic1['b'])
# print(dic2)