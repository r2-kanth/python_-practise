from functools import reduce
l = [23.445,34,67,34,23,6,5,3,345,56,5]

def Greater(a, b):
    if (a > b):
        return a
    return b

print(reduce(Greater , l))