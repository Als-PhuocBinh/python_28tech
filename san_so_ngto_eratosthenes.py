#check số nguyên tố bình thường: O(N*can n)
#sàng số nguyên tố: O(NlogNlogN)
#bội của một số nguyên tố thì không phải là số nguyên tố
#sử dụng kĩ thuật mảng đánh dấu
from math import *
prime  = [True] * (10**6 + 1)
def sieve():
    prime[0] = prime[1] = False
    for i in range(2, isqrt(10**6 + 1) + 1):
        if prime[i]:
            for j in range(i*i, 10**6 + 1, i):
                prime[j] = False

if __name__ == '__main__':
    sieve()
    for i in range(1001):
        if prime[i]: print(i, end = ' ')