from math import *
F1 = [1] * (10**6 + 1)
def giaiThua():
    for i in range(2, 10**6 + 1):
        F1[i] = F1[i-1] * i
        F1[i] %= (10**9 + 7)

F2 = [0] * (10**6 + 1)
def fibo():
    F2[0], F2[1] = 0, 1
    for i in range(2, 10**6 + 1):
        F2[i] = F2[i-2] + F2[i-1]
        F2[i] %= (10**9 + 7)

Fnt = [True] * (10**6 + 1)
def sieve():
    Fnt[0], Fnt[1] = False, False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if Fnt[i]:
            for j in range(i*i, 10**6+1, i):
                Fnt[j] = False

F3 = [0] * (10**6 + 1)
def cntFrime():
    F3[0], F3[1] = 0, 0
    cnt = 0
    for i in range(2, 10**6 + 1):
        if Fnt[i]:
            cnt += 1
        F3[i] = cnt
        
F4 = [0] * (10**6 + 1)
def tichNgTo():
    res = 1
    for i in range(2, 10**6 + 1):
        if Fnt[i]:
            res = res * i % (10**9 + 7)
        F4[i] = res

if __name__ == '__main__':
    n = int(input())
    sieve()
    tichNgTo()
    for i in range(n):
        x = int(input())
        print(F4[x]) #O(1)