from math import *
from functools import cmp_to_key
# sắp xếp dãy số theo tổng chữ số tăng dần, nếu cùng tổng thì số bé xếp trước

def sum_digit(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

def cmp(a, b):
    tong1, tong2 = sum_digit(a), sum_digit(b)
    if tong1 == tong2:
        return a - b
    else:
        return tong1 - tong2
if __name__ == '__main__':
    a = [100, 10, 61, 5, 8, 4, 21, 53, 7]
    a.sort(key = cmp_to_key(cmp))
    print(a)