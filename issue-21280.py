import numpy as np
class myarr(np.ndarray):
    __array_priority__ = -1

class non_myarr(np.ndarray):
    __array_non_priority__ = -1

a = np.arange(3)
b = np.arange(3).view(myarr)

print("a")
print(a)
print("b")
print(b)
print("np multiply a, b: ")
print(type(np.multiply(a, b)))
print("np multiply b, a: ")
print(type(np.multiply(b, a))) 

# although priority is negative, `myarr` is used:
assert type(np.multiply(a, b)) is non_myarr
assert type(np.multiply(b, a)) is myarr

# But this is not true for the Python helper:
res = np.arange(3)
assert type(np.get_array_wrap(a, b)(res)) is np.ndarray
