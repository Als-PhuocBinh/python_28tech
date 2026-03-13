from math import *
a = (8, 9, 1, 2, 7, 4, 5, 10)
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
nt_a = [x**5 for x in a if nt(x)]
print(nt_a)
b = list(filter(lambda x: x > 5, a))
print(b)